variable "base_bucket_name" {
  default = "datalake-felipe-xpe-tf"
}

variable "environment" {
  default = "production"
}

variable "account_number" {
  default = "689150947157"
}

locals {
  aws_region = "us-east-2"
}

