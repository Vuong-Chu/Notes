# Notes

### 1. RESTful API: 
* API stands for Application Programming Interface and it basically allows a piece of software to talk to another.
* REST stands for REpresentational State Transfer. This essentially refers to a style of web architecture that has many underlying characteristics and governs the behavior of clients and servers. 
* REST is defined by 6 constraints: client-server, stateless, cacheable, layered system, uniform interface, code on demand:

  * _Uniform interface_: A resource in the system should have only one logical URI, and that should provide a way to fetch related or additional data. It’s always better to synonymize a resource with a web page. Any single resource should not be too large and contain each and everything in its representation. Whenever relevant, a resource should contain links (HATEOAS) pointing to relative URIs to fetch related information.
  * _Client–server_: Client application and server application MUST be able to evolve separately without any dependency on each other. A client should know only resource URIs while server should know only database and data on the server.
  * _Stateless_: The server will not store anything about the latest HTTP request the client made. It will treat every request as new. No session, no history.
  * _Cacheable_: The caching of data and responses is of utmost importance wherever they are applicable/possible. Caching brings performance improvement for the client-side and better scope for scalability for a server because the load has reduced.
  * _Layered system_: REST allows you to use a layered system architecture where you deploy the APIs on server A, and store data on server B and authenticate requests in Server C, for example. A client cannot ordinarily tell whether it is connected directly to the end server or an intermediary along the way.
  * _Code on demand (optional)_:


[Click to read more](https://github.com/Vuong-Chu/Notes/blob/main/Web%20API%20Design%20The%20Missing%20Link.pdf).

### 2. Docker:
