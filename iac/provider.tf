provider "aws" {
  region = "us-east-2"
}

terraform {
  backend "s3" {
    bucket = "terraform-state-felipe"
    key = "state/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}
