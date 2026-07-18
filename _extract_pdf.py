"""Extract text from Williamson & van der Mark (1997) PDF."""
import sys, re, os

sys.path.insert(0, r'C:\Users\LENOVO\AppData\Local\Programs\Python\Python312\Lib\site-packages')

path = os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'DeepChat',
    'alpha-pi-helix-repo', 'alpha-pi-helix', 'v1.2', 'literature',
    'williamson-van-der-mark-1997.pdf')

try:
    from PyPDF2 import PdfReader
    reader = PdfReader(path)
    print(f'Pages: {len(reader.pages)}')
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            print(f'\n=== Page {i+1} ===')
            print(text[:4000])
except ImportError:
    print('PyPDF2 not installed. Trying raw text extraction...')
    try:
        with open(path, 'rb') as f:
            content = f.read()
        text = content.decode('latin-1', errors='ignore')
        
        # Search for key terms
        keywords = ['Compton', 'torus', 'radius', 'photon confined', 
                    'wavelength', 'fine-structure', 'electron radius',
                    'classical electron', 'helical', 'toroidal', 'topology',
                    'equation', 'alpha', 'vortex', 'ring']
        
        for kw in keywords:
            for m in re.finditer(re.escape(kw), text, re.IGNORECASE):
                idx = m.start()
                context = text[max(0,idx-80):idx+300]
                context = re.sub(r'[^\x20-\x7E\n]', '', context)
                print(f'\n--- "{kw}" ---')
                print(context[:500])
                break  # first occurrence only
    except Exception as e:
        print(f'Error: {e}')
