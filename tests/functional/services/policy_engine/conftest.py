import pytest
from tests.functional.services.policy_engine.utils import (images_api,
                                                           registry_api, utils)
from tests.functional.services.utils import http_utils

# This list of tags from the docker.io/anchore/test_images repo will get automatically added as part of
# the pytest session
TEST_IMAGE_TAGS = [
    # Leaving some out now so the test doesn't take forever to run
    # NOTE: the images/test_list_images test verifies the anchore/test_images:npm image as part of the test,
    # so don't add it here
    # "py38",
    # "java",
    # "gems",
    # "debian-stretch-slim",
    # "centos8",
    # "bin",
    # "spring",
    "lean",
    # "alpine_eicar_malware_test",
    # "alpine_clean",
    # "allthethings_v1",
]

# This is a map of image tag to a dict containing the image_digest, potentially more information as tests are developed
TEST_IMAGES_MAP = {}


@pytest.fixture(scope="session")
def add_dockerhub_registry(request) -> None:
    registry_info = utils.get_registry_info()
    registry_kwargs = {
        "registry": registry_info["host"],
        "registry_name": registry_info["service_name"],
        "registry_pass": registry_info["pass"],
        "registry_type": "docker_v2",
        "registry_user": registry_info["user"],
        "registry_verify": False,
    }
    registry_api.post_registry(**registry_kwargs)

    def remove_registry():
        registry_api.delete_registry("docker.io")

    request.addfinalizer(remove_registry)


@pytest.fixture(scope="session", autouse=True)
def add_test_images(request, add_dockerhub_registry) -> None:
    """
    Leverages the add_dockerhub_registry fixture so that we don't run into rate limiting issues
    """
    image_digests = []
    for test_image_tag in TEST_IMAGE_TAGS:
        full_tag = "docker.io/anchore/test_images:%s" % test_image_tag
        image: http_utils.APIResponse = images_api.post_image(full_tag)
        image_digest = utils.get_image_digest(image)
        TEST_IMAGES_MAP[full_tag] = {"imageDigest": image_digest}
        image_digests.append(image_digest)
        utils.wait_for_image(test_image_tag, image_digest)

    def remove_test_images():
        for image_digest in image_digests:
            images_api.delete_image(image_digest)

    request.addfinalizer(remove_test_images)


@pytest.fixture(scope="session")
def test_images_map():
    return TEST_IMAGES_MAP
