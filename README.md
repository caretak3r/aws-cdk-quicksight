# Quicksight

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


## Requirements
1. Classes to encapsulate common configuration items.
2. Classes to encapsulate QS asset mappings. 
3. 