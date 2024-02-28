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
  image_name   = var.dev_deploy_image_name
  ssh_username = var.ssh_username
  zone         = var.zone
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
    generated   = true
  }
  provisioner "shell" {
    scripts = [
      "./packer_setup/setup_dependencies.sh",
    ]
  }
}
