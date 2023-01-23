variable "aws_region" {
  default = "us-east-2"
}

provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = "terraform-state-felipe"
    key = "state/edc/mod1/terraform.tfstate"
    region = var.aws_region
  }
}
