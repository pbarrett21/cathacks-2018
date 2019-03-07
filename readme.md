# Alexa Notetaker

**Cathacks 2018 Submission**

**Josh Baunach and Paul Barrett**

This is the code for an Alexa skill that captures notes from meetings.

## Directories

### lambda/

This directory corresponds to the code that ran in the Lambda on AWS. It contains the lambda code itself as well as its dependencies.

The lambda was written in Python. It was spun off the sample Lambda code that was provided by Amazon, so at the time this Readme was written, there are still remnants of code from that sample.

When Alexa hears an intent combined with the invocation for the skill, the Lambda will find the matching intent and make a POST request to Josh's DigitalOcean server with the information from Alexa.

### server/

This directory contains the server-side code. This code ran on a DigitalOcean Droplet.

The code is written in Python and has not much more functionality than responding to POST and GET requests sent by the Lambda and the client site, respectively. In the POST request, it will append the parameters to a list of parameters that have been captured in the current session. In the GET request, it will send all of the parameters that have been captured over the session.

### site/

This directory contains the client-side site code. It does not need to run on a server; it can run on a local machine.

The code for getting data from the server was written in JavaScript. The Materialize library was used to style the site. Every half second, the site will make a GET request to the server. The server will respond with the parameters it captured from the AWS Lambda, and the site will format it into proper HTML and display it to the user.
