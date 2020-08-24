Vagrant.configure("2") do |config|
  config.vm.box = "geerlingguy/centos8"

  am_vm_name = "ansible-molecule"

  config.vm.define am_vm_name do |am|
    am.vm.provider "virtualbox" do |vb|
      vb.name = am_vm_name
      vb.cpus = 3
      vb.memory = 3072
    end
    am.vm.hostname = am_vm_name
  end

  config.vm.provision "shell", inline: "yum install -y git python3-pip yum-utils vim tree"
  config.vm.provision "shell", inline: "pip3 install ansible==2.9.12 ansible-lint==4.3.0"
  config.vm.provision "shell", inline: "pip3 install molecule==3.0.7 docker"
  config.vm.provision "shell", inline: "yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo"
  config.vm.provision "shell", inline: "yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm"
  config.vm.provision "shell", inline: "yum install -y docker-ce docker-ce-cli containerd.io"
  config.vm.provision "shell", inline: "systemctl start docker"
  config.vm.provision "shell", inline: "usermod -G docker -a vagrant"
end
