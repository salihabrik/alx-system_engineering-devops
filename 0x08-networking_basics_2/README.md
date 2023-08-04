# Loopback
The local loopback mechanism may be used to run a network service on a host without requiring a physical network interface, or without making the service accessible from the networks the computer may be connected to. For example, a locally installed website may be accessed from a Web browser by the URL http://localhost to display its home page.

The name localhost normally resolves to the IPv4 loopback address 127.0.0.1, and to the IPv6 loopback address ::1.[1]

Name resolution
IPv4 network standards reserve the entire address block 127.0.0.0/8 (more than 16 million addresses) for loopback purposes.[2] That means any packet sent to any of those addresses is looped back. The address 127.0.0.1 is the standard address for IPv4 loopback traffic; the rest are not supported by all operating systems. However, they can be used to set up multiple server applications on the host, all listening on the same port number. The IPv6 standard assigns only a single address for loopback: ::1.IANA, who allocate IP addresses globally, have allocated the single IP address 0.0.0.0[1] to RFC 1122 section 3.2.1.3. It is named as "This host on this network".

RFC 1122 refers to 0.0.0.0 using the notation {0,0}. It prohibits this as a destination address in IPv4 and only allows it as a source address under specific circumstances.

A host may use 0.0.0.0 as its own source address in IP when it has not yet been assigned an address, such as when sending the initial DHCPDISCOVER packet when using DHCP.
![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Internet_map_1024_-_transparent%2C_inverted.png/150px-Internet_map_1024_-_transparent%2C_inverted.png)



