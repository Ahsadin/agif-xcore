"""Policy modules consumed by the AGIF-XCore client and proxy.

v0.3: ``tool_policy`` declares per-tool allow/soften/block decisions plus
optional argument-pattern deny rules. The module lives here (not under
``proxy/``) because ``client.py`` consumes it and the client layer must not
depend on the proxy layer.
"""
