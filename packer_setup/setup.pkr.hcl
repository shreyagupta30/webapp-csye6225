source "googlecompute" "centos-csye" {
  project_id          = var.project_id
  source_image_family = var.source_image_family
  image_name          = var.image_name
  image_description   = "A custom CentOS Stream 8 image with Python installed"
  ssh_username        = var.ssh_username
  zone                = var.zone
  network             = var.network
}

source "googlecompute" "centos-csye-deploy" {
  project_id   = var.project_id
  source_image = var.image_name
  zone         = var.zone
  ssh_username = var.ssh_username
  image_name   = var.dev_deploy_image_name
}

build {
  sources = ["sources.googlecompute.centos-csye"]

  provisioner "shell" {
    scripts = [
      "./packer_setup/setup_db.sh",
    ]
  }
}

build {
  sources = ["source.googlecompute.centos-csye-deploy"]
  provisioner "file" {
    source      = "csye6225.zip"
    destination = "/tmp/csye6225.zip"
    generated   = "true"
  }
  provisioner "shell" {
    scripts = [
      "./packer/scripts/setup_dependencies.sh",
    ]
  }
}
