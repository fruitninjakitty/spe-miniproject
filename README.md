# spe-miniproject
CSE806-Software Production Engineering Miniproject creating a CI/CD pipeline using Jenkins, Docker, Ansible and GitHub for a scientific calculator.

Name: Jaskirat Singh Sanghera

Roll Number: PGP2024011

# Calculator CI/CD Pipeline

This project demonstrates a CI/CD pipeline for a command-line calculator application using:
- Jenkins for continuous integration
- Docker for containerization
- Ansible for deployment automation
- ngrok for exposing the application
- GitHub for source code management

## Features

The calculator supports the following operations:
- Square Root
- Factorial
- Natural Logarithm
- Exponentiation

## Pipeline Steps

1. Code is pushed to GitHub
2. Jenkins pulls the code and runs tests
3. Docker builds an image of the application
4. Ansible deploys the Docker container
5. ngrok exposes the application publicly
