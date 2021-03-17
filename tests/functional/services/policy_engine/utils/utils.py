import os
import time
from typing import Dict

from tests.functional.services.policy_engine.utils import images_api
from tests.functional.services.utils import http_utils


def get_registry_info() -> Dict[str, str]:
    return {
        "user": os.getenv("DOCKER_USER"),
        "pass": os.getenv("DOCKER_PASS"),
        "host": os.getenv("DOCKER_HOST", "docker.io"),
        "service_name": "DockerHub",
    }


def wait_for_image(
    image_tag: str,
    image_digest: str,
    retry_limit: int = -1,
) -> None:
    if not image_tag:
        raise ValueError("Cannot wait for image without image_tag")
    if not image_digest:
        raise ValueError("Cannot wait for image without image_digest")

    analysis_status = "analyzing"
    tries = 0
    while analysis_status != "analyzed" and (retry_limit != -1 or tries >= retry_limit):
        tries += 1
        print(
            "waiting for image to analyze: tag=%s, digest=%s"
            % (image_tag, image_digest)
        )
        add_image_resp = images_api.get_image(image_digest)

        if add_image_resp and len(add_image_resp.body) > 0:
            analysis_status = get_analysis_status(add_image_resp)
            if analysis_status != "analyzed":
                time.sleep(5)


def get_image_digest(api_resp: http_utils.APIResponse) -> str:
    return api_resp.body[0].get("imageDigest")


def get_analysis_status(api_resp: http_utils.APIResponse) -> str:
    return api_resp.body[0].get("analysis_status")
