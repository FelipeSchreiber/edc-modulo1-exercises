resource "aws_s3_bucket" "datalake" {
    bucket = "${var.base_bucket_name}-${var.environment}-${var.account_number}"
    acl = "private"
    server_side_encryption_configuration {
      rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
        }
      }
    }
  tags = {
    "CURSO" = "EDC"
  }
}