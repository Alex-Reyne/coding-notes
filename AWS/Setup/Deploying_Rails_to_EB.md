# AWS

## Deploy Rails to Elastic Beanstalk
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ruby-rails-tutorial.html
```sh
# Create Elastic Beanstalk Environment
# Create new rails project

# Update Gemfile for successful deployment w/ Elastic Beanstalk
# add `platform ruby` to Gemfile.lock so required dependencies are installed with deployment
bundle lock --add-platform ruby

# Add environment properties

# Deploy application
# Create source bundle zip file
zip ../rails-default.zip -r * .[^.]*
# Upload source bundle to Elastic Beanstalk to deploy rails environment

```
