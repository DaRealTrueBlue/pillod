# Publishing Pillod to PyPI

This guide walks you through publishing the pillod package to PyPI so others can install it with `pip install pillod`.

## Prerequisites

1. **Python 3.7+** installed
2. **A PyPI account** - Sign up at https://pypi.org
3. **Git** (optional, but recommended)

## Step-by-Step Instructions

### 1. Install Required Tools

Open PowerShell and run:

```powershell
pip install --upgrade setuptools wheel twine
```

These tools are needed to build and upload your package.

### 2. Update setup.py

Edit [setup.py](setup.py) and update:
- `author` - Your name
- `author_email` - Your email address
- `url` - Link to your GitHub repository (e.g., `https://github.com/yourusername/pillod`)

Example:
```python
author="John Doe",
author_email="john@example.com",
url="https://github.com/johndoe/pillod",
```

### 3. Update LICENSE

Edit [LICENSE](LICENSE) and replace "Your Name" and the year with your information.

### 4. Create .pypirc Configuration File

This file stores your PyPI credentials securely.

**Windows:** Create file `C:\Users\<YourUsername>\.pypirc`

Add this content (replace with your PyPI username):
```ini
[distutils]
index-servers =
    pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = <your-pypi-token>
```

**Note:** You'll get a token in step 6.

### 5. Generate PyPI Token

1. Go to https://pypi.org/account/ and log in
2. Go to **Account Settings** → **API tokens**
3. Click **Add API token**
4. Name it "pillod" and select "Entire account"
5. Copy the token (looks like `pypi-AgE...`)
6. Paste it in `.pypirc` as shown above

**Important:** Keep this token secret! Don't share it or commit it to GitHub.

### 6. Build Your Package

Navigate to your project directory in PowerShell:

```powershell
cd C:\Users\ewl57\Documents\Pillod
```

Build the distribution files:

```powershell
python setup.py sdist bdist_wheel
```

This creates a `dist/` folder with:
- `pillod-0.2.0.tar.gz` (source distribution)
- `pillod-0.2.0-py3-none-any.whl` (wheel distribution)

### 7. Test Your Package Locally

Before uploading to PyPI, test in a clean environment:

```powershell
# Create a test virtual environment
python -m venv test_env
test_env\Scripts\activate

# Install from local dist
pip install C:\Users\ewl57\Documents\Pillod\dist\pillod-0.2.0-py3-none-any.whl

# Test import
python -c "import pillod; print(pillod.__version__)"

# Deactivate
deactivate
```

### 8. Upload to TestPyPI (Optional but Recommended)

Test uploading to TestPyPI first (no real consequences if something goes wrong):

```powershell
twine upload --repository testpypi dist/*
```

Visit https://test.pypi.org/project/pillod/ to verify it looks good.

### 9. Upload to Real PyPI

Once satisfied, upload to the real PyPI:

```powershell
twine upload dist/*
```

You'll be prompted for your username and password (use `__token__` as username and your token as password).

**Success!** Your package is now on PyPI!

### 10. Install Your Package from PyPI

Anyone (including you!) can now install it:

```powershell
pip install pillod
```

Then use it in Python:

```python
import pillod

name = pillod.parsertools.ask_string("What's your name? ")
password = pillod.randomtools.random_password()
print(f"Hello {name}! Your password is {password}")
```

## Managing Updates

When you update your package:

1. Update the version in `setup.py`:
   ```python
   version="0.3.0",  # Changed from 0.2.0
   ```

2. Rebuild:
   ```powershell
   rm dist/*  # Clean old builds
   python setup.py sdist bdist_wheel
   ```

3. Re-upload:
   ```powershell
   twine upload dist/*
   ```

## Troubleshooting

**Issue: "Invalid credentials"**
- Check your `.pypirc` file exists and has correct token
- Make sure username is `__token__` (not your PyPI username)

**Issue: "Package name already exists"**
- PyPI requires unique package names
- Change `name` in setup.py to something unique
- Check https://pypi.org to see if name is taken

**Issue: "twine: command not found"**
- Run: `pip install twine`

**Issue: Build fails**
- Make sure README.md exists
- Verify setup.py syntax
- Run: `python -m twine check dist/*` to validate

## Resources

- [PyPI Official Docs](https://packaging.python.org/)
- [setuptools Documentation](https://setuptools.pypa.io/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [TestPyPI](https://test.pypi.org/)

## Next Steps

After publishing:
1. Add to GitHub and share the link
2. Create releases on GitHub for each version
3. Add GitHub Actions for automated testing
4. Consider adding a CI/CD pipeline for automatic PyPI uploads

Good luck! 🚀
