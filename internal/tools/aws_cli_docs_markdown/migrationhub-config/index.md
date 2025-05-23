# migrationhub-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# migrationhub-config

## Description

The AWS Migration Hub home region APIs are available specifically for working with your Migration Hub home region. You can use these APIs to determine a home region, as well as to create and work with controls that describe the home region.

- You must make API calls for write actions (create, notify, associate, disassociate, import, or put) while in your home region, or a `HomeRegionNotSetException` error is returned.
- API calls for read actions (list, describe, stop, and delete) are permitted outside of your home region.
- If you call a write API outside the home region, an `InvalidInputException` is returned.
- You can call `GetHomeRegion` action to obtain the accountâs Migration Hub home region.

For specific API usage, see the sections that follow in this AWS Migration Hub Home Region API reference.

## Available Commands

- [create-home-region-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/create-home-region-control.html)
- [delete-home-region-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/delete-home-region-control.html)
- [describe-home-region-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/describe-home-region-controls.html)
- [get-home-region](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/get-home-region.html)