# Scikit-learn Installation Guide

## Multiple Installation Options

### Option 1: Latest Version (Recommended)
```bash
pip install scikit-learn
```

### Option 2: Specific Compatible Version
```bash
pip install scikit-learn==1.2.2
```

### Option 3: Legacy Systems
```bash
pip install scikit-learn==1.1.3
```

### Option 4: Minimal Installation
```bash
pip install scikit-learn==1.0.2 numpy==1.21.0 scipy==1.7.0
```

## If Installation Fails

### Windows Issues
```bash
# Try with --no-cache-dir
pip install --no-cache-dir scikit-learn

# Or use conda instead
conda install scikit-learn

# Or use pre-compiled wheels
pip install --only-binary=all scikit-learn
```

### Alternative: Use requirements-legacy.txt
```bash
pip install -r requirements-legacy.txt
```

## Test Installation
```python
import sklearn
print(f"Scikit-learn version: {sklearn.__version__}")
from sklearn.ensemble import RandomForestClassifier
print("✅ Installation successful!")
```

## Common Issues & Solutions

**Issue**: `Microsoft Visual C++ 14.0 is required`
**Solution**: Install Visual Studio Build Tools or use conda

**Issue**: `Failed building wheel for scikit-learn`
**Solution**: 
```bash
pip install --upgrade pip setuptools wheel
pip install scikit-learn
```

**Issue**: Import errors
**Solution**: 
```bash
pip uninstall scikit-learn
pip install scikit-learn --no-deps
pip install numpy scipy joblib threadpoolctl
```