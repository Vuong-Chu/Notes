# Notes of Software Engineering

### 1. RESTful API: 
* API stands for Application Programming Interface and it basically allows a piece of software to talk to another.
* REST stands for REpresentational State Transfer. This essentially refers to a style of web architecture that has many underlying characteristics and governs the behavior of clients and servers. 
* REST is defined by 6 constraints: client-server, stateless, cacheable, layered system, uniform interface, code on demand:

  * __Uniform interface__: A resource in the system should have only one logical URI, and that should provide a way to fetch related or additional data. It’s always better to synonymize a resource with a web page. Any single resource should not be too large and contain each and everything in its representation. Whenever relevant, a resource should contain links (HATEOAS) pointing to relative URIs to fetch related information.
  * __Client–server__: Client application and server application MUST be able to evolve separately without any dependency on each other. A client should know only resource URIs while server should know only database and resource on the server.
  * __Stateless__: The server will not store anything about the latest HTTP request the client made. It will treat every request as new. No session, no history.
  * __Cacheable__: The caching of data and responses is of utmost importance wherever they are applicable/possible. Caching brings performance improvement for the client-side and better scope for scalability for a server because the load has reduced.
  * __Layered system__: REST allows you to use a layered system architecture where you deploy the APIs on server A, and store data on server B and authenticate requests in Server C, for example. A client cannot ordinarily tell whether it is connected directly to the end server or an intermediary along the way.
  * __Code on demand (optional)__: Most of the time, you will be sending the static representations of resources in the form of XML or JSON. But when you need to, you are free to return executable code to support a part of your application.

[Click to read more](https://github.com/Vuong-Chu/Notes/blob/main/SWE/Web%20API%20Design%20The%20Missing%20Link.pdf).

### 2. Docker:
- The machine on which Docker is installed and running is usually referred to as a Docker Host. whenever you plan to deploy an application on the host, it would create a logical entity on it to host that application. In Docker terminology, we call this logical entity a Container or Docker Container to be more precise. Docker builds containers for you containing everything required to run the code. A Docker Container doesn’t have any operating system installed and running on it. But it would have a virtual copy of the process table, network interface(s), and the file system mount point(s). These have been inherited from the operating system of the host on which the container is hosted and running. This allows each container to be isolated from the other present on the same host.
- Docker would virtualize the operating system of the host on which it is installed and running, rather than virtualizing the hardware components. So, applications with different operating system requirements cannot be hosted together on the same Docker Host. For example, let’s say we have 4 different applications, out of which 3 applications require a Linux-based operating system and the other application requires a Windows-based operating system. In such a scenario, the 3 applications that require Linux-based operating system can be hosted on a single Docker Host, whereas the application that requires a Windows-based operating system needs to be hosted on a different Docker Host.
- Core component of Docker
 * Docker Engine is one of the core components of Docker. It is responsible for the overall functioning of the Docker platform. It includes:
  *  Server: Server runs a daemon known as __dockerd (Docker Daemon)__, which is nothing but a process. It is responsible for creating and managing Docker Images, Containers, Networks and Volumes on the Docker platform.
  *  REST API: REST API specifies how the applications can interact with the Server, and instruct it to get their job done.
  *  Client: a command line interface, that allows users to interact with Docker using the commands.
- Docker terminology
 * Docker Image is a template that contains the application, and all the dependencies required to run that application on Docker.
 * Docker Container is a logical entity. In more precise terms, it is a running instance of the Docker Image.
 * Docker Hub is the official online repository where you could find all the Docker Images that are available for us to use. It also allows us to store and distribute our custom images as well if we wish to do so. We could also make them either public or private, based on our requirements.
- Docker syntax
 * docker create [options] IMAGE [commands] [arguments]
 * docker start [options] CONTAINER ID/NAME [CONTAINER ID/NAME…]
 * docker rm [options] CONTAINER ID/NAME [CONTAINER ID/NAME...]
 * docker rmi [options] IMAGE NAME/ID [IMAGE NAME/ID...]
 Anything enclosed within the square brackets is optional. This is applicable to all the commands that you would see on this guide.
