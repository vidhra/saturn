# lex-runtimeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# lex-runtime

## Description

Amazon Lex provides both build and runtime endpoints. Each endpoint provides a set of operations (API). Your conversational bot uses the runtime API to understand user utterances (user input text or voice). For example, suppose a user says âI want pizzaâ, your bot sends this input to Amazon Lex using the runtime API. Amazon Lex recognizes that the user request is for the OrderPizza intent (one of the intents defined in the bot). Then Amazon Lex engages in user conversation on behalf of the bot to elicit required information (slot values, such as pizza size and crust type), and then performs fulfillment activity (that you configured when you created the bot). You use the build-time API to create and manage your Amazon Lex bot. For a list of build-time operations, see the build-time API, .

## Available Commands

- [delete-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/delete-session.html)
- [get-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/get-session.html)
- [post-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/post-content.html)
- [post-text](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/post-text.html)
- [put-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/put-session.html)