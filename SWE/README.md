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
__Docker Engine__ is one of the core components of Docker. It is responsible for the overall functioning of the Docker platform. It includes:
  *  Server: Server runs a daemon known as __dockerd (Docker Daemon)__, which is nothing but a process. It is responsible for creating and managing Docker Images, Containers, Networks and Volumes on the Docker platform.
  *  REST API: REST API specifies how the applications can interact with the Server, and instruct it to get their job done.
  *  Client: a command line interface, that allows users to interact with Docker using the commands.
__Docker terminology__
 * Docker Image is a template that contains the application, and all the dependencies required to run that application on Docker.
 * Docker Container is a logical entity. In more precise terms, it is a running instance of the Docker Image.
 * Docker Hub is the official online repository where you could find all the Docker Images that are available for us to use. It also allows us to store and distribute our custom images as well if we wish to do so. We could also make them either public or private, based on our requirements.
__Docker syntax__
 * docker create [options] IMAGE [commands] [arguments] (Create an image)
 * docker start [options] CONTAINER ID/NAME [CONTAINER ID/NAME…] (Start a container)
 * docker kill [options] CONTAINER ID/NAME [CONTAINER ID/NAME…] (Stop a container)
 * docker rm [options] CONTAINER ID/NAME [CONTAINER ID/NAME...] (Remove a container)
 * docker rmi [options] IMAGE NAME/ID [IMAGE NAME/ID...] (Remove image)
 * docker ps -a/--format $FORMAT/-l --format=$FORMAT (View info)
 * docker run -ti ubuntu:latest bash (Run an image => creating an instance of the image, which is a container)
 * docker run --rm -ti ubuntu:latest bash (Run and automatically remove container after exit)
 * docker run -d -ti ubuntu:latest bash (Run a container under the background)/docker attach IMAGE ID/NAME (Recall a container under the background)
 * docker exec -ti IMAGE ID/NAME (Run more things in a container)
 * docker commit IMAGE NAME/ID[:tags] (Create an image from container)
 * docker logs CONTAINER ID/NAME (To keep output of containers)
 * docker run --memory/--cpu-share (To limit resources for running a container)
 * docker run -rm -ti -p xxx:xxxx -p yyyy:yyyy --name SERVER NAME ubuntu:14.04 bash (expose fixed ports)
   *  nc -lp xxxx | nc -lp yyyy (lp-listen on port)
   *  nc localhost xxxx
   *  nc host.docker.internal xxxx
 * docker run -rm -ti -p xxx -p yyyy --name SERVER NAME ubuntu:14.04 bash (expose dynamic ports)
 * docker port SERVER NAME
   * nc -lp xxxx | nc -lp yyyy (lp-listen on port)
   * nc local host zzzz
 * docker run -rm -ti -net learning --name SERVER NAME
   * nc -lp xxxx
   * nc SERVER NAME xxxx
 * docker network connect SERVER NAME1 SERVER NAME2
 Anything enclosed within the square brackets is optional. This is applicable to all the commands that you would see on this guide.
 Notes: Don't let containers fetch depenencies when they start. Don't leave important things in unnamed and stopped containers.
 ### 3. Maven:
 Maven is a powerful build tool for Java software projects. A build tool is a tool that automates everything related to building the software project. Building a software project typically includes one or more of these activities:
  * Generating source code.
  * Generating documentation from the source code.
  * Compiling source code.
  * Packaging compiled code into JAR files or ZIP files.
  * Installing the packaged code on a server, in a repository or somewhere else.
One of the first goals Maven executes is to check the dependencies needed by your project. The advantage of automating the build process is that you minimize the risk of humans making errors while building the software manually. Additionally, an automated build tool is typically faster than a human performing the same steps manually. 
Maven is centered around the concept of POM files (Project Object Model). A POM file is an XML representation of project resources like source code, test code, dependencies (external JARs used) etc. The POM contains references to all of these resources. When you execute a Maven command you give Maven a POM file to execute the commands on. Maven will then execute the command on the resources described in the POM. The POM file describes what to build, but most often not how to build it.
__Maven POM file__
  * The modelVersion element sets what version of the POM model you are using.
  * The groupId element is a unique ID for an organization, or a project (an open source project, for instance). Most often you will use a group ID which is similar to the root Java package name of the project. group ID does not have to be a Java package name, and does not need to use the . notation (dot notation) for separating words in the ID. But, if you do, the project will be located in the Maven repository under a directory structure matching the group ID.
  * The artifactId element contains the name of the project you are building. The artifact ID is also used as part of the name of the JAR file produced when building the project.
  * The versionId element contains the version number of the project. If your project has been released in different versions, for instance an open source API, then it is useful to version the builds.

All Maven POM files inherit from a super POM. If no super POM is specified, the POM file inherits from the base POM. An inheriting POM file may override settings from a super POM. Just specify new settings in the inheriting POM file.

Types of dependencies: An __external dependency__ in Maven is a dependency (JAR file) which is not located in a Maven repository (neither local, central or remote repository). It may be located somewhere on your local hard disk, for instance in the lib directory of a webapp, or somewhere else. The word "external" thus means external to the Maven repository system - not just external to the project. Most dependencies are external to the project, but few are external to the repository system (not located in a repository). __Snapshot dependencies__ are dependencies (JAR files) which are under development. Instead of constantly updating the version numbers to get the latest version, you can depend on a snapshot version of the project. Snapshot versions are always downloaded into your local repository for every build, even if a matching snapshot version is already located in your local repository. Always downloading the snapshot dependencies assures that you always have the latest version in your local repository, for every build. If your project depends on a dependency, say Dependency ABC, and Dependency ABC itself depends on another dependency, say Dependency XYZ, then your project has a __transitive dependency__ on Dependency XYZ. You can specify a __dependency exclusion__ inside the declaration of the dependency which transitive dependency you want to exclude.

Unless your project is small, your project may need external Java APIs or frameworks which are packaged in their own JAR files. These JAR files are needed on the classpath when you compile your project code. Keeping your project up-to-date with the correct versions of these external JAR files can be a comprehensive task. Each external JAR may again also need other external JAR files etc. Downloading all these external dependencies (JAR files) recursively and making sure that the right versions are downloaded is cumbersome. Especially when your project grows big, and you get more and more external dependencies. Luckily, Maven has built-in dependency management. You specify in the POM file what external libraries your project depends on, and which version, and then Maven downloads them for you and puts them in your local Maven repository. If any of these external libraries need other libraries, then these other libraries are also downloaded into your local Maven repository.

Maven Repositories: Maven repositories are directories of packaged JAR files with extra meta data. The meta data are POM files describing the projects each packaged JAR file belongs to, including what external dependencies each packaged JAR has. This meta data enables Maven to download dependencies of your dependencies recursively, until the whole tree of dependencies is download and put into your local repository. A __local repository__ is a directory on the developer's computer. This repository will contain all the dependencies Maven downloads. The same Maven repository is typically used for several different projects. By default Maven puts your local repository inside your user home directory on your local computer. However, you can change the location of the local repository by setting the directory inside your Maven settings file. Your Maven settings file is also located in your user-home/.m2 directory and is called settings.xml. But, for more convinience, we can update setting Maven in Intellij. The __central Maven__ repository is a repository provided by the Maven community. By default Maven looks in this central repository for any dependencies needed but not found in your local repository. Maven then downloads these dependencies into your local repository. You need no special configuration to access the central repository. A __remote repository__ is a repository on a web server from which Maven can download dependencies, just like the central repository. A remote repository can be located anywhere on the internet, or inside a local network. A remote repository is often used for hosting projects internal to your organization, which are shared by multiple projects. You can configure a remote repository in the POM file. Put the following XML elements right after the <dependencies> element.
 
Maven can build a Fat JAR from your Java project. A Fat JAR is a single JAR file that contains all the compiled Java classes from your project, and all compiled Java classes from all JAR files your project depends on. You can package your microservice and all of its dependencies into a single JAR file. This makes execution much easier, because you don't have to list all the JAR files your microservice depends on, on the classpath. Fat JARs are also handy if you need to package your application inside a Docker container. Instead of having to add each JAR file your application depends on to the Docker container, you only have to add the Fat JAR of our application.

 ### 4. Linux:
 
```
```
 ### 5. Concurrency:
<p align="center">
  <img src="threadmodel.png" width="900" height="467">
</p>
  
