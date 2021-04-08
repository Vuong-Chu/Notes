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

  * An application client or applet and components running on the Java EE server.

  * Server components and a database.

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

#### 1.3. Web Services Support
Web services are web-based enterprise applications that use open, XML-based standards and transport protocols to exchange data with calling clients. To write web services and clients with the Java EE XML APIs, all you need to do is pass parameter data to the method calls and process the data returned; for document-oriented web services, you send documents containing the service data back and forth. The translation of data to a standardized XML-based data stream is what makes web services and clients written with the Java EE XML APIs fully interoperable.

* XML: Extensible Markup Language (XML) is a cross-platform, extensible, text-based standard for representing data.

* SOAP Transport Protocol: Client requests and web service responses are transmitted as Simple Object Access Protocol (SOAP) messages over HTTP to enable a completely interoperable exchange between clients and web services, all running on different platforms and at various locations on the Internet. HTTP is a familiar request-and-response standard for sending messages over the Internet, and SOAP is an XML-based protocol that follows the HTTP request-and-response model. The SOAP portion of a transported message does the following:

  * Defines an XML-based envelope to describe what is in the message and explain how to process the message.

  * Includes XML-based encoding rules to express instances of application-defined data types within the message.

  * Defines an XML-based convention for representing the request to the remote service and the resulting response.

* WSDL Standard Format: The Web Services Description Language (WSDL) is a standardized XML format for describing network services. The description includes the name of the service, the location of the service, and ways to communicate with the service. WSDL service descriptions can be published on the Web.

#### 1.4. Java EE APIs
Enterprise JavaBeans Technology: An Enterprise JavaBeans (EJB) component, or enterprise bean, is a body of code that has fields and methods to implement modules of business logic. Enterprise beans either session beans or message-driven beans:

* A session bean represents a transient conversation with a client. When the client finishes executing, the session bean and its data are gone.
* A message-driven bean combines features of a session bean and a message listener, allowing a business component to receive messages asynchronously. Commonly, these are Java Message Service (JMS) messages.

Java Servlet Technology: Java Servlet technology lets you define HTTP-specific servlet classes. A servlet class extends the capabilities of servers that host applications accessed by way of a request-response programming model.

JavaServer Faces Technology: JavaServer Faces technology is a user interface framework for building web applications. The main components of JavaServer Faces technology are as follows:
* A GUI component framework.
* A flexible model for rendering components in different kinds of HTML or different markup languages and technologies.
* A standard RenderKit for generating HTML 4.01 markup.

JavaServer Pages Technology: JavaServer Pages (JSP) technology lets you put snippets of servlet code directly into a text-based document.

JavaServer Pages Standard Tag Library: The JavaServer Pages Standard Tag Library (JSTL) encapsulates core functionality common to many JSP applications. This standardization allows you to deploy your applications on any JSP container that supports JSTL and makes it more likely that the implementation of the tags is optimized.

Java Persistence API: The Java Persistence API (JPA) is a Java standards–based solution for persistence. Persistence uses an object/relational mapping approach to bridge the gap between an object-oriented model and a relational database.

Java Transaction API: The Java Transaction API (JTA) provides a standard interface for demarcating transactions. The Java EE architecture provides a default auto commit to handle transaction commits and rollbacks. An auto commit means that any other applications that are viewing data will see the updated data after each database read or write operation. However, if your application performs two separate database access operations that depend on each other, you will want to use the JTA API to demarcate where the entire transaction, including both operations, begins, rolls back, and commits.

Java API for RESTful Web Services: APIs for the development of web services built according to the Representational State Transfer (REST) architectural style. A JAX-RS application is a web application that consists of classes packaged as a servlet in a WAR file along with required libraries.

Managed Beans: These are lightweight container-managed objects (POJOs) with minimal requirements, support a small set of basic services, such as resource injection, lifecycle callbacks, and interceptors. Managed Beans represent a generalization of the managed beans specified by JavaServer Faces technology and can be used anywhere in a Java EE application, not just in web modules.

Contexts and Dependency Injection for Java EE: Contexts and Dependency Injection for Java EE (CDI) defines a set of contextual services, provided by Java EE containers, that make it easy for developers to use enterprise beans along with JavaServer Faces technology in web applications. In other hand, Dependency Injection for Java defines a standard set of annotations (and one interface) for use on injectable classes.

Bean Validation: The Bean Validation specification defines a metadata model and API for validating data in JavaBeans components. Instead of distributing validation of data over several layers, such as the browser and the server side, you can define the validation constraints in one place and share them across the different layers.

Java Message Service API: The Java Message Service (JMS) API is a messaging standard that allows Java EE application components to create, send, receive, and read messages. It enables distributed communication that is loosely coupled, reliable, and asynchronous.

Java EE Connector Architecture: The Java EE Connector Architecture is used by tools vendors and system integrators to create resource adapters that support access to enterprise information systems that can be plugged in to any Java EE product.

JavaMail API: Java EE applications use the JavaMail API to send email notifications. The JavaMail API has two parts:

* An application-level interface used by the application components to send mail

* A service provider interface

Java Authorization Contract for Containers: The Java Authorization Contract for Containers (JACC) specification defines a contract between a Java EE application server and an authorization policy provider. All Java EE containers support this contract.

Java Authentication Service Provider Interface for Containers: The Java Authentication Service Provider Interface for Containers (JASPIC) specification defines a service provider interface (SPI) by which authentication providers that implement message authentication mechanisms may be integrated in client or server message-processing containers or runtimes. Authentication providers integrated through this interface operate on network messages provided to them by their calling containers. The authentication providers transform outgoing messages so that the source of each message can be authenticated by the receiving container, and the recipient of the message can be authenticated by the message sender. Authentication providers authenticate each incoming message and return to their calling containers the identity established as a result of the message authentication.

Java EE Security API: The Java EE Security API specification defines portable, plug-in interfaces for HTTP authentication and identity stores, and an injectable SecurityContext interface that provides an API for programmatic security.

Java API for WebSocket: WebSocket is an application protocol that provides full-duplex communications between two peers over TCP. The Java API for WebSocket enables Java EE applications to create endpoints using annotations that specify the configuration parameters of the endpoint and designate its lifecycle callback methods.

Java API for JSON Processing: JavaScript Object Notation (JSON) is a text-based data exchange format derived from JavaScript that is used in web services and other connected applications. The Java API for JSON Processing (JSON-P) enables Java EE applications to parse, transform, and query JSON data using the object model or the streaming model.

Java API for JSON Binding: The Java API for JSON Binding (JSON-B) provides a binding layer for converting Java objects to and from JSON messages. JSON-B also supports the ability to customize the default mapping process used in this binding layer through the use of Java annotations for a given field, JavaBean property, type or package, or by providing an implementation of a property naming strategy.

Concurrency Utilities for Java EE: Concurrency Utilities for Java EE is a standard API for providing asynchronous capabilities to Java EE application components through the following types of objects: managed executor service, managed scheduled executor service, managed thread factory, and context service.

Batch Applications for the Java Platform: Batch jobs are tasks that can be executed without user interaction. The Batch Applications for the Java Platform specification is a batch framework that provides support for creating and running batch jobs in Java applications.

Java Database Connectivity API: The Java Database Connectivity (JDBC) API lets you invoke SQL commands from Java programming language methods. You use the JDBC API in an enterprise bean when you have a session bean access the database. You can also use the JDBC API from a servlet or a JSP page to access the database directly without going through an enterprise bean.

Java Naming and Directory Interface API: The Java Naming and Directory Interface (JNDI) API provides naming and directory functionality, enabling applications to access multiple naming and directory services, such as LDAP, DNS, and NIS. The JNDI API provides applications with methods for performing standard directory operations, such as associating attributes with objects and searching for objects using their attributes. Using JNDI, a Java EE application can store and retrieve any type of named Java object, allowing Java EE applications to coexist with many legacy applications and systems.

JavaBeans Activation Framework: The JavaBeans Activation Framework (JAF) is used by the JavaMail API. JAF provides standard services to determine the type of an arbitrary piece of data, encapsulate access to it, discover the operations available on it, and create the appropriate JavaBeans component to perform those operations.

Java API for XML Processing: The Java API for XML Processing (JAXP), part of the Java SE platform, supports the processing of XML documents using Document Object Model (DOM), Simple API for XML (SAX), and Extensible Stylesheet Language Transformations (XSLT). JAXP enables applications to parse and transform XML documents independently of a particular XML-processing implementation.

Java Architecture for XML Binding: The Java Architecture for XML Binding (JAXB) provides a convenient way to bind an XML schema to a representation in Java language programs. JAXB can be used independently or in combination with JAX-WS, in which case it provides a standard data binding for web service messages. All Java EE application client containers, web containers, and EJB containers support the JAXB API.

Java API for XML Web Services: The Java API for XML Web Services (JAX-WS) specification provides support for web services that use the JAXB API for binding XML data to Java objects. The JAX-WS specification defines client APIs for accessing web services as well as techniques for implementing web service endpoints.

SOAP with Attachments API for Java: The SOAP with Attachments API for Java (SAAJ) is a low-level API on which JAX-WS depends. SAAJ enables the production and consumption of messages that conform to the SOAP 1.1 and 1.2 specifications and the SOAP with Attachments note. Most developers do not use the SAAJ API, instead using the higher-level JAX-WS API.

Java Authentication and Authorization Service: The Java Authentication and Authorization Service (JAAS) provides a way for a Java EE application to authenticate and authorize a specific user or group of users to run it.

Common Annotations for the Java Platform: Annotations enable a declarative style of programming in the Java platform.





#### 2. JavaSE
##### 2.1 JavaFX
Types of binding:

** High level:

 ** Fluent API:
 
    ```
    //Area = Side x Side
    IntegerProperty Area = new SimpleIntegerProperty();
    IntegerProperty Side = new SimpleIntegerProperty();
    Area.bind(Side.multiply(Side));
    ```
    
 ** Binding class:
 
     ```
    //Area = Side x Side
    IntegerProperty Area = new SimpleIntegerProperty();
    IntegerProperty Side = new SimpleIntegerProperty();
    NumberBinding squareBinding = Bindings.multiply(Side,Side);
    Area.bind(squareBinding);
    ```
    
** Low level:

    ```
    IntegerProperty Side = new SimpleIntegerProperty();
    IntegerBinding Area = new IntegerBinding(){
      {
      super.bind(Area);
      }
      @Overide
      protected int computeValue(){
        return Side.get() * Side.get();
      }
    };
    ```

