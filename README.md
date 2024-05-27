# Data-Protection-using-Steganography-and-Cryptography

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<p>Welcome to the Steganography and Cryptography Portal! This application allows you to hide text in audio files, text in images, and images within images using steganographic techniques.</p>

<h2>Features</h2>
<ul>
    <li><strong>Text in Audio</strong>: Hide text messages within audio files.</li>
    <li><strong>Text in Image</strong>: Hide text messages within image files.</li>
    <li><strong>Image in Image</strong>: Hide one image within another image.</li>
</ul>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.x</li>
    <li>Required Python libraries: <code>stegano</code>, <code>Pillow</code>, <code>twofish</code>, <code>memory_profiler</code>, <code>wave</code></li>
</ul>

<h2>Installation</h2>
<p>To get started, clone this repository and install the necessary dependencies:</p>
<pre>
<code>
git clone https://github.com/pranjalgautam11/Data-Protection-using-Steganography-and-Cryptography.git
pip install -r requirements.txt
</code>
</pre>

<h2>Usage</h2>
<p>Run the main script to access the Steganography and Cryptography Portal:</p>
<pre>
<code>
python menudriven.py
</code>
</pre>
<p>You will be presented with a menu to choose from different steganographic techniques:</p>
<pre>
<code>
Welcome to Steganography and Cryptography Portal

Enter 1: text in audio
Enter 2: text in image
Enter 3: image in image
Enter 0: Exit
Choice: 
</code>
</pre>

<h3>Options</h3>
<ol>
    <li><strong>Text in Audio</strong>: Enter <code>1</code> to hide text within an audio file. This will invoke the <code>aud_steg()</code> function from the <code>textinaudio</code> module.</li>
    <li><strong>Text in Image</strong>: Enter <code>2</code> to hide text within an image file. This will invoke the <code>incript()</code> function from the <code>textinimage</code> module.</li>
    <li><strong>Image in Image</strong>: Enter <code>3</code> to hide one image within another image. This will invoke the <code>image_steg()</code> function from the <code>imageinimage</code> module.</li>
    <li><strong>Exit</strong>: Enter <code>0</code> to exit the portal.</li>
</ol>

<h2>Modules</h2>
<h3>textinaudio.py</h3>
<p>Provides functions to encode and decode text messages in audio files using the LSB (Least Significant Bit) technique. Also supports encryption and decryption of the encoded audio files.</p>

<h3>textinimage.py</h3>
<p>Provides functions to encode and decode text messages in image files by modifying pixel values. Also supports encryption and decryption of the encoded image files.</p>

<h3>imageinimage.py</h3>
<p>Provides functions to encode and decode images within other images using the LSB technique. Also supports encryption and decryption of the encoded image files.</p>

<h2>Authors</h2>
<p>Developed by:</p>
<ul>
    <li><strong>Pranjal Gautam</strong> - <a href="mailto:pranjalgautam1103@gmail.com">pranjalgautam1103@gmail.com</a></li>
    <li><strong>Bhargavi Joshi</strong> - <a href="mailto:bhargavijoshi86@gmail.comm">bhargavijoshi86@gmail.com</a></li>
</ul>

</body>
</html>
