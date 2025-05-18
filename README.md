# Sphinx-Project-Example

A simple CLI library system implemented in Python. This repository serves as an example project for demonstrating CI/CD practices, particularly the use of Jenkins and Docker to automatically deploy Sphinx-generated documentation.

## Features

- Basic command-line interface for managing a library system
- Structured to support Sphinx documentation generation
- CI/CD pipeline setup with Jenkins and Docker for automated documentation deployment

## Getting Started

### Prerequisites

- Python 3.x
- [Docker](https://www.docker.com/get-started)
- [Jenkins](https://www.jenkins.io/) (optional, for local testing of the pipeline)
- [Sphinx](https://www.sphinx-doc.org/) (for building documentation locally)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AndykingSkywalker/Sphinx-Project-Example.git
   cd Sphinx-Project-Example
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run the CLI library system:
```bash
python main.py
```
*(Assuming `main.py` is the entry point. Update if your entry point differs.)*

Follow the on-screen prompts to use the library management features.

## Sphinx Documentation

To build the documentation locally:
```bash
cd docs
make html
```
The generated documentation can be found in `docs/_build/html`.

## CI/CD Pipeline

This repository is configured to demonstrate:

- **Jenkins Pipeline**: For automating tests and documentation builds.
- **Docker**: To encapsulate the build and deployment process.

On each commit or pull request, Jenkins will:

1. Build and test the project.
2. Generate Sphinx documentation.
3. Deploy the documentation using Docker.

Refer to the `Jenkinsfile` and `Dockerfile` for pipeline implementation details.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

---

*Project maintained by [AndykingSkywalker](https://github.com/AndykingSkywalker).*
