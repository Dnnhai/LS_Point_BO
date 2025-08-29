# LS Point BO - Automation Test with Playwright-pytest

## 1. Pull Docker Image
```bash
docker pull ghcr.io/dnnhai/ls_point_bo:latest
```

## 2. Run Tests without Report 
	(Quick check to verify the container runs correctly)
```bash
docker run --rm ghcr.io/dnnhai/ls_point_bo:latest
```

---

## 3. Set up Allure (Windows)

### a. Allow to run script 
```powershell
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
```

### b. Setup Scoop (package manager)
```powershell
irm get.scoop.sh | iex
```

### c. setup Allure via Scoop
```powershell
scoop install allure
```

### d. Add PATH to Environment
Example:
```
C:\Users\Admin\scoop\apps\allure\2.34.1\bin
```

---

## 4. Run Tests with Report
```bash
docker run --rm -v ${PWD}\allure-results:/app/allure-results ghcr.io/dnnhai/ls_point_bo pytest --alluredir=/app/allure-results -v
```

---

## 5. View Allure Report
Stay in the folder that contains `allure-results`, then run:
```bash
allure serve allure-results
```

---
