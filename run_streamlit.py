#!/usr/bin/env python3
"""
Script to run the Vet Heart Care Streamlit application
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit application"""
    print("🩺 Starting Vet Heart Care - Sistema de Laudos")
    print("=" * 50)
    
    # Check if streamlit is installed
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit>=1.28.0"])
    
    # Check if template file exists
    template_path = os.path.join(os.path.dirname(__file__), 'heartcaresite', 'upload_folder', 'Laudo Eco Modelo P.docx')
    if not os.path.exists(template_path):
        print(f"⚠️  Warning: Template file not found at {template_path}")
        print("   Make sure the template file exists before generating documents.")
    
    # Run streamlit
    print("\n🚀 Launching Streamlit application...")
    print("   The app will open in your default web browser.")
    print("   Press Ctrl+C to stop the application.\n")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"❌ Error running Streamlit: {e}")

if __name__ == "__main__":
    main()

