import sys

import yarl

from .._core import HttpCore
from .._helper import log_success, pack_form_request, parse_json, send_request
from ..const import APP_BASE_HOST, APP_SECURE_SCHEME
from ..exception import TiebaServerError


def parse_body(body: bytes) -> None:
    res_json = parse_json(body)
    if code := int(res_json['error_code']):
        raise TiebaServerError(code, res_json['error_msg'])


async def request(http_core: HttpCore, fid: int, tid: int, is_hide: bool) -> bool:
    data = [
        ('BDUSS', http_core.core._BDUSS),
        ('fid', fid),
        ('is_frs_mask', int(is_hide)),
        ('tbs', http_core.core._tbs),
        ('z', tid),
    ]

    request = pack_form_request(
        http_core,
        yarl.URL.build(scheme=APP_SECURE_SCHEME, host=APP_BASE_HOST, path="/c/c/bawu/delthread"),
        data,
    )

    __log__ = f"fid={fid} tid={tid}"

    body = await send_request(request, http_core.connector, read_bufsize=1024)
    parse_body(body)

    log_success(sys._getframe(1), __log__)
    return True