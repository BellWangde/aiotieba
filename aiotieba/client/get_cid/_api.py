from typing import Dict

import aiohttp
import yarl

from .._core import TbCore
from .._helper import pack_form_request, parse_json, send_request
from ..const import APP_BASE_HOST, APP_SECURE_SCHEME
from ..exception import TiebaServerError


def parse_body(body: bytes) -> Dict[str, str]:
    res_json = parse_json(body)
    if code := int(res_json['error_code']):
        raise TiebaServerError(code, res_json['error_msg'])

    cates = res_json['cates']

    return cates


async def request(connector: aiohttp.TCPConnector, core: TbCore, fname: str) -> Dict[str, str]:
    data = [
        ('BDUSS', core._BDUSS),
        ('word', fname),
    ]

    request = pack_form_request(
        core,
        yarl.URL.build(scheme=APP_SECURE_SCHEME, host=APP_BASE_HOST, path="/c/c/bawu/goodlist"),
        data,
    )

    __log__ = "fname={fname}"  # noqa: F841

    body = await send_request(request, connector, read_bufsize=1024)
    return parse_body(body)