# Django REST Framework tutorial 
This repository cover a simple code for creating a highlighted Web API using Django REST framework.
Documentation Link- https://www.django-rest-framework.org/tutorial/1-serialization/

## Project Flow-


### _Serialization_
Serializers allow complex data like querysets and model instances to be converted to Python datatypes, and these can be further rendered into JSON, XML or other types. Deserializers allow parsed data to be converted back into complex types, after validating the incoming data.

     1.  Created a new project REST_framework. Start an app named Snippet, add both to settings file. 
     2. Create a model to store code snippets inside snippet app, define required fields, sync the database.
     3. Make a new file for defining serializers, create a Serializer class for serializing and deserializing of 
        snippet instances.
     4. Create few snippet instances using python shell.
     5 . ModelSerializer class can be used to make code more concise.
     6. Create views defining that you want your API to display or function, then add these to urls file.
     7. Now, test your API, you will see the JSON formatted content displayed.


### _Request and Responses_
REST framework's Request class extends the regular HttpRequest, provide support for REST framework's flexible request parsing and authentication. REST framework introduces a Response object, that takes unrendered content and uses content negotiation to determine the correct content type to return to the client.

     1. In this section, Rest framework core functions are used like request and response objects, status codes, API wrappers.
     2. REST framework provides two types of API warppers you can use while writing views, these provide more functionalities 
        like handling exceptions, dealing with request and response objects.
     3. Format suffix pattern added to urls so that now our API will be able to handle URLs for specific formats requested.


### _Class based Views_
Class based views are helpful in a way that these allows us to reuse the common functionality in our code.

     1. Now we will rewrite our API using class based views and refactor snippet/urls.py file accordingly.
     2. Using Mixin classes- these provides implementation of common behaviours like update/delete/create.
     3. Using the GenericAPIView class to provide the core functionality, and mixins to provide the
      .retrieve(), .update () and .destroy() actions.


### _Authentication and Permissions_
In this part, we will adding some restrictions like who can access our API. We will add some advanced behaviours to make
sure that only authenticated users can update code snippets and unauthenticated users will have read-only access.

     1. Firstly, add a field to store owner information and one for highlighted HTML representation in your model.
     2. Add endpoint for user model, associate snippets with users, update serializer file.
     3. Add required permissions to views, update urls file. 



### _Hyperlinked API's and Relationships_
Hyperlinking for relationships are used to improve discoverability of API's. Hyperlinked style is used between entities.
Now, you can work around your API simply by following links in your web browser.

     1. Created an endpoint for root of API and highlghted snippets- added views for the same.
     2. For hyperlinking, we will modify our serialiizers file, we will use HyperlinkedModelSerializer 
        instead of ModelSerializer.
     3. Here, relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
     4. Edit url patterns for new changes.

### _Viewsets and Routers_
 A ViewSet class is a set of method handlers that provide operations such as retrieve, or update. Router class handles the complexities of defining the URL configurations.

     1. Refactor previously written views using viewsets.
     2. Binding viewsets to urls- In the snippets/urls.py file ,bind ViewSet classes into a set of concrete views.
     3. Use routers for designing URL conf- register viewsets with router and it will automatically handle the conventions.
