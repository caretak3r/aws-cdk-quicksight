# Quicksight

## Context && Problem 

### Specific Example

## Determined Solution

### Requirements


## Notes 
    - use `aws_cdk.aws_quicksight.CfnTemplate` to create a template from existing analysis or template
        - A template adds a layer of abstraction by using placeholders to replace the dataset associated with an analysis. You can use templates to create dashboards by replacing dataset placeholders with datasets that follow the same schema that was used to create the source analysis and template.


## Process

1. Create datasource. 
2. Create dataset from datasource.
    a. Define ingestion(Quicksight refresh) policies
    b. Define data transformations
    c. Rename columns
    d. Add calculated fields
3. Create analysis. 
4. Create template
5. Create a dashboard from templates.

## How Developers use Quicksight
1. Generally using snowflake datasource could be wrapped with a data set. 
2. Create new datasets, configure them, select columns. 
3. Share datasets.
4. Create multiple analyses based on 1 dataset. 
5. Share analysis.
6. Multiple analyses can create any number of dashboards (panels/frames are in a dashboard). 
    a. Whatever is generated from the link (embedded dashboard) is a dashboard with an id.
7. Publish dashboards.
8. Maintain permissions.

## Requirements
1. Classes to encapsulate common configuration items.
2. Classes to encapsulate QS asset mappings. 
3. 


## References
1. https://aws.amazon.com/blogs/business-intelligence/automate-and-accelerate-your-amazon-quicksight-asset-deployments-using-the-new-apis/
2. https://constructs.dev/packages/@aws-cdk/aws-quicksight/v/1.204.0?lang=python
3. 