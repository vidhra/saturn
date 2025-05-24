# cleanroomsmlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# cleanroomsml

## Description

Welcome to the *Amazon Web Services Clean Rooms ML API Reference* .

Amazon Web Services Clean Rooms ML provides a privacy-enhancing method for two parties to identify similar users in their data without the need to share their data with each other. The first party brings the training data to Clean Rooms so that they can create and configure an audience model (lookalike model) and associate it with a collaboration. The second party then brings their seed data to Clean Rooms and generates an audience (lookalike segment) that resembles the training data.

To learn more about Amazon Web Services Clean Rooms ML concepts, procedures, and best practices, see the [Clean Rooms User Guide](https://docs.aws.amazon.com/clean-rooms/latest/userguide/machine-learning.html) .

To learn more about SQL commands, functions, and conditions supported in Clean Rooms, see the [Clean Rooms SQL Reference](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference.html) .

## Available Commands

- [cancel-trained-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/cancel-trained-model.html)
- [cancel-trained-model-inference-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/cancel-trained-model-inference-job.html)
- [create-audience-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-audience-model.html)
- [create-configured-audience-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-configured-audience-model.html)
- [create-configured-model-algorithm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-configured-model-algorithm.html)
- [create-configured-model-algorithm-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-configured-model-algorithm-association.html)
- [create-ml-input-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-ml-input-channel.html)
- [create-trained-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-trained-model.html)
- [create-training-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/create-training-dataset.html)
- [delete-audience-generation-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-audience-generation-job.html)
- [delete-audience-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-audience-model.html)
- [delete-configured-audience-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-configured-audience-model.html)
- [delete-configured-audience-model-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-configured-audience-model-policy.html)
- [delete-configured-model-algorithm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-configured-model-algorithm.html)
- [delete-configured-model-algorithm-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-configured-model-algorithm-association.html)
- [delete-ml-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-ml-configuration.html)
- [delete-ml-input-channel-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-ml-input-channel-data.html)
- [delete-trained-model-output](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-trained-model-output.html)
- [delete-training-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/delete-training-dataset.html)
- [get-audience-generation-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-audience-generation-job.html)
- [get-audience-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-audience-model.html)
- [get-collaboration-configured-model-algorithm-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-collaboration-configured-model-algorithm-association.html)
- [get-collaboration-ml-input-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-collaboration-ml-input-channel.html)
- [get-collaboration-trained-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-collaboration-trained-model.html)
- [get-configured-audience-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-configured-audience-model.html)
- [get-configured-audience-model-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-configured-audience-model-policy.html)
- [get-configured-model-algorithm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-configured-model-algorithm.html)
- [get-configured-model-algorithm-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-configured-model-algorithm-association.html)
- [get-ml-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-ml-configuration.html)
- [get-ml-input-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-ml-input-channel.html)
- [get-trained-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-trained-model.html)
- [get-trained-model-inference-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-trained-model-inference-job.html)
- [get-training-dataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-training-dataset.html)
- [list-audience-export-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-audience-export-jobs.html)
- [list-audience-generation-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-audience-generation-jobs.html)
- [list-audience-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-audience-models.html)
- [list-collaboration-configured-model-algorithm-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-collaboration-configured-model-algorithm-associations.html)
- [list-collaboration-ml-input-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-collaboration-ml-input-channels.html)
- [list-collaboration-trained-model-export-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-collaboration-trained-model-export-jobs.html)
- [list-collaboration-trained-model-inference-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-collaboration-trained-model-inference-jobs.html)
- [list-collaboration-trained-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-collaboration-trained-models.html)
- [list-configured-audience-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-configured-audience-models.html)
- [list-configured-model-algorithm-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-configured-model-algorithm-associations.html)
- [list-configured-model-algorithms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-configured-model-algorithms.html)
- [list-ml-input-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-ml-input-channels.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-tags-for-resource.html)
- [list-trained-model-inference-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-trained-model-inference-jobs.html)
- [list-trained-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-trained-models.html)
- [list-training-datasets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/list-training-datasets.html)
- [put-configured-audience-model-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/put-configured-audience-model-policy.html)
- [put-ml-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/put-ml-configuration.html)
- [start-audience-export-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/start-audience-export-job.html)
- [start-audience-generation-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/start-audience-generation-job.html)
- [start-trained-model-export-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/start-trained-model-export-job.html)
- [start-trained-model-inference-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/start-trained-model-inference-job.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/untag-resource.html)
- [update-configured-audience-model](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/update-configured-audience-model.html)