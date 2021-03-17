from tests.functional.services.utils import http_utils


def post_image(
    image_tag: str,
) -> http_utils.APIResponse:
    if not image_tag:
        raise ValueError("Cannot add image without image_tag")
    print("Adding image: tag=%s" % image_tag)
    add_image_resp = http_utils.http_post(["images"], {"tag": image_tag})
    if add_image_resp.code != 200:
        raise http_utils.RequestFailedError(
            add_image_resp.url, add_image_resp.code, add_image_resp.body
        )
    return add_image_resp


def get_image(
    image_digest: str,
) -> http_utils.APIResponse:
    if not image_digest:
        raise ValueError("Cannot get image without image_digest")
    get_image_resp = http_utils.http_get(["images", image_digest])
    if get_image_resp.code != 200:
        raise http_utils.RequestFailedError(
            get_image_resp.url, get_image_resp.code, get_image_resp.body
        )
    return get_image_resp


def delete_image(
    image_digest: str,
) -> http_utils.APIResponse:
    if not image_digest:
        raise ValueError("Cannot delete image without image_digest")
    delete_image_resp = http_utils.http_del(["images", image_digest])
    if delete_image_resp.code != 200:
        raise http_utils.RequestFailedError(
            delete_image_resp.url, delete_image_resp.code, delete_image_resp.body
        )
    return delete_image_resp
