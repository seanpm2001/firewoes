# The settings defined here will override those defined in webconfig.py

# database
DATABASE_URI = "postgresql://matthieu:matthieu@localhost:5432/firewose"

# the url pattern used to generate urls to point on source code
DEBIAN_SOURCES_URL = "http://sources.debian.net/src/{package}/{version}-{release}/{path}?msg={message}&hl={lines_range}#L{anchor}"

FEDORA_SOURCES_URL = "http://foo.bar"

# the url pattern used for embedded source code
DEBIAN_EMBEDDED_SOURCES_URL = "http://sources.debian.net/embedded/{package}/{version}-{release}/{path}?msg={message}&hl={lines_range}#L{anchor}"

FEDORA_EMBEDDED_SOURCES_URL = "http://foo.bar"

# where one can find the source code of the app
GITWEB_URL = "http://git.upsilon.cc/?p=firewose.git"
