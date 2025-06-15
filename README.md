Hello, this is VK simple service.
This time, when creating VkAPi, we do not use a username/password, but an access key. After that, we create a message queue that we want to listen to.
For communities, you need to use the VkBotLongPoll class, which accepts the connection session and the community ID (you can see it in the link to the community page — these are just numbers). 
If we are not acting as a community, but as a user, we need to use the VkLongPoll class. After that, we start an endless cycle of waiting for messages in our queue.
If a message of the VkBotEventType.MESSAGE_NEW type arrives, we display the message itself (there is a lot of interesting information there), then the user ID—the author of the message and the text of the message.
In addition, we can immediately respond to the user by calling the messages.send service.
For a correct call, it is necessary to pass the user_id — the identifier of the user or group chat where we are writing the message, the text of the message message, as well as a large random number of random_ids, which is necessary in order not to send the user the same messages several times.
I think I'll deal with this powerful VK API later and post a few additional features.
The time has come. I used some of the code from a previous project. You can use this bot for a simple service.
See you soon

Last change: I have things to do in the next few days, I think when I get back I'll finalize a few features in this project and take part in a code marathon (maybe I'll create a new repository for it)
