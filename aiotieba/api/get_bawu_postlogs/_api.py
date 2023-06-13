import bs4
import yarl

from ...const import WEB_BASE_HOST
from ...core import HttpCore
from ...request import pack_web_get_request, send_request
from ._classdef import Postlogs


def parse_body(body: bytes) -> Postlogs:
    soup = bs4.BeautifulSoup(body, 'lxml')
    bawu_postlogs = Postlogs(soup)

    return bawu_postlogs


async def request(http_core: HttpCore, fname: str, pn: int) -> Postlogs:
    params = [
        ('word', fname),
        ('pn', pn),
        ('ie', 'utf-8'),
    ]

    request = pack_web_get_request(
        http_core,
        yarl.URL.build(scheme="https", host=WEB_BASE_HOST, path="/bawu2/platform/listPostLog"),
        params,
    )

    __log__ = "fname={fname}"  # noqa: F841

    body = await send_request(request, http_core.network, read_bufsize=64 * 1024)
    return parse_body(body)