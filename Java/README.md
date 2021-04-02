# Notes on Java

### 1. JavaEE
#### 1.1. Distributed Multitiered Applications
The aim of the Java EE platform is to provide developers with a powerful set of APIs while shortening development time, reducing application complexity, and improving application performance.

The Java EE platform uses a simplified programming model. A developer can simply enter the information as an annotation directly into a Java source file, and the Java EE server will configure the component at deployment and runtime. These annotations are generally used to embed in a program data that would otherwise be furnished in a deployment descriptor. With annotations, you put the specification information in your code next to the program element affected.

In the Java EE platform, dependency injection can be applied to all resources a component needs, effectively hiding the creation and lookup of resources from application code. Dependency injection can be used in Enterprise JavaBeans (EJB) containers, web containers, and application clients. Dependency injection allows the Java EE container to automatically insert references to other required components or resources, using annotations.

Java EE applications are made up of components. A Java EE component is a self-contained functional software unit that is assembled into a Java EE application with its related classes and files and that communicates with other components.

The Java EE specification defines the following Java EE components:

* Application clients and applets are components that run on the client.

* Java Servlet, JavaServer Faces, and JavaServer Pages (JSP) technology components are web components that run on the server.

* EJB components (enterprise beans) are business components that run on the server.

**Java EE Clients**:
* Web Clients: Dynamic webs and Web browsers. A web client is sometimes called a thin client. Thin clients usually do not query databases, execute complex business rules, or connect to legacy applications. When you use a thin client, such heavyweight operations are off-loaded to enterprise beans executing on the Java EE server, where they can leverage the security, speed, services, and reliability of Java EE server-side technologies.

* Application Clients: An application client runs on a client machine and provides a way for users to handle tasks that require a richer user interface than can be provided by a markup language. Application clients directly access enterprise beans running in the business tier. However, if application requirements warrant it, an application client can open an HTTP connection to establish communication with a servlet running in the web tier. Application clients written in languages other than Java can interact with Java EE servers, enabling the Java EE platform to interoperate with legacy systems, clients, and non-Java languages.

* Applets: A web page received from the web tier can include an embedded applet. Written in the Java programming language, an applet is a small client application that executes in the Java virtual machine installed in the web browser.

* Javabean Component Archietecture: The server and client tiers might also include components based on the JavaBeans component architecture (JavaBeans components) to manage the data flow between the following:

 * An application client or applet and components running on the Java EE server

 * Server components and a database

JavaBeans components are not considered Java EE components by the Java EE specification. JavaBeans components have properties and have get and set methods for accessing those properties. JavaBeans components used in this way are typically simple in design and implementation but should conform to the naming and design conventions outlined in the JavaBeans component architecture.
* Java Server Communications: The client communicates with the business tier running on the Java EE server either directly or, as in the case of a client running in a browser, by going through web pages or servlets running in the web tier.
  
**Web Components**: 
Java EE web components are either servlets or web pages created using JavaServer Faces technology and/or JSP technology (JSP pages). 

* Servlets are Java programming language classes that dynamically process requests and construct responses. 
* JSP pages are text-based documents that execute as servlets but allow a more natural approach to creating static content. 
* JavaServer Faces technology builds on servlets and JSP technology and provides a user interface component framework for web applications.

**Business Components**:
Business code, which is logic that solves or meets the needs of a particular business domain such as banking, retail, or finance, is handled by enterprise beans running in either the business tier or the web tier.

**Enterpise Information System Tier**:
The enterprise information system tier handles EIS software and includes enterprise infrastructure systems, such as enterprise resource planning (ERP), mainframe transaction processing, database systems, and other legacy information systems.

<p align="center">
  <img src="javaeett_dt_004.png" width="513" height="537">
</p>
#### 1.2. Java EE Containers
Containers are the interface between a component and the low-level, platform-specific functionality that supports the component. Before it can be executed, a web, enterprise bean, or application client component must be assembled into a Java EE module and deployed into its container.

Container types:
* Java EE server: The runtime portion of a Java EE product. A Java EE server provides EJB and web containers.

* EJB container: Manages the execution of enterprise beans for Java EE applications. Enterprise beans and their container run on the Java EE server.

* Web container: Manages the execution of web pages, servlets, and some EJB components for Java EE applications. Web components and their container run on the Java EE server.

* Application client container: Manages the execution of application client components. Application clients and their container run on the client.

* Applet container: Manages the execution of applets. Consists of a web browser and a Java Plug-in running on the client together.

<p align="center">
  <img src="javaeett_dt_005.png" width="513" height="537">
</p>

#### 2. JavaSE
