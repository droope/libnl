"""Netlink Types (netlink-private/types.h).
https://github.com/thom311/libnl/blob/master/include/netlink-private/types.h

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation version 2.1
of the License.
"""

from libnl.linux_private.netlink import sockaddr_nl

NL_SOCK_BUFSIZE_SET = 1 << 0
NL_SOCK_PASSCRED = 1 << 1
NL_OWN_PORT = 1 << 2
NL_MSG_PEEK = 1 << 3
NL_NO_AUTO_ACK = 1 << 4
NL_MSG_CRED_PRESENT = 1


class nl_cb(object):  # TODO
    """Netlink callback class (C struct equivalent).
    https://github.com/thom311/libnl/blob/master/include/netlink-private/types.h#L39

    Instance variables:
    cb_set -- dictionary of callback functions (values), indexed by callback type (keys).
    cb_args -- dictionary of arguments to be passed to callback functions (values), indexed by callback type (keys).
    cb_err -- error callback function.
    cb_err_arg -- argument to be passed to error callback function.
    cb_recvmsgs_ow -- TODO
    cb_recv_ow -- TODO
    cb_send_ow -- call this function instead of nl_send_iovec() in nl_send(). Args are (sk, msg).
    cb_active -- current callback type (e.g. NL_CB_MSG_OUT). Modified before every callback function call.
    """

    def __init__(self):
        self.cb_set = dict()
        self.cb_args = dict()
        self.cb_err = None
        self.cb_err_arg = None
        self.cb_recvmsgs_ow = None
        self.cb_recv_ow = None
        self.cb_send_ow = None
        self.cb_active = None


class nl_sock(object):
    """Netlink socket class (C struct equivalent).
    https://github.com/thom311/libnl/blob/master/include/netlink-private/types.h#L69

    Instance variables:
    s_local -- struct sockaddr_nl.
    s_peer -- struct sockaddr_nl.
    s_fd -- returns -1 if the socket has not been opened, or the socket's file descriptor integer.
    s_proto -- int.
    s_seq_next -- unsigned int.
    s_seq_expect -- unsigned int.
    s_flags -- int.
    s_cb -- struct nl_cb.
    s_bufsize -- size_t.
    socket_instance -- the actual socket.socket() instance.
    """

    def __init__(self):
        self.s_local = sockaddr_nl()
        self.s_peer = sockaddr_nl()
        self.s_proto = 0
        self.s_seq_next = 0
        self.s_seq_expect = 0
        self.s_flags = 0
        self.s_cb = None
        self.s_bufsize = None
        self.socket_instance = None

    @property
    def s_fd(self):
        return -1 if self.socket_instance is None else self.socket_instance.fileno()


class nl_msg(object):
    """https://github.com/thom311/libnl/blob/master/include/netlink-private/types.h#L133"""

    def __init__(self):
        self.nm_protocol = 0
        self.nm_flags = 0
        self.nm_src = sockaddr_nl()
        self.nm_dst = sockaddr_nl()
        self.nm_creds = None
        self.nm_nlh = None
        self.nm_refcnt = 0