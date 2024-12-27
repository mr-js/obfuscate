# obfuscate
 Obfuscate your file names for privacy and compress your photos for speed and space

 ## Usage
 Just run the program and follow instructions
 
 > [!WARNING]
 > Be careful! If you select the "Write changes" option (unchecked by default), the obfuscation/compression of all files in the specified directory will be performed immediately, and there will be no way back -- it will be impossible to restore the previous file names (since the purpose of the program is obfuscation without the possibility of recovery).
 > During processing, even with filename obfuscation turned off, all files are recreated based on their contents, which resets basic attributes (e.g., date and time of creation and modification).

 ## Examples

 ### Obfuscation

 **Sample random files**
 ```
 IMG_64790832_02.JPG -> GPFA5JYM.jpg
 MyBirthday_2008.mp4 -> CT6LQSFG.mp4
 AllPasswords_01.doc -> S6P45UHJ.doc
 ```

 ### Compression

 **Sample photo #1 ORIGINAL (11.1MB)**
 ![original](/images/original.jpg)
 
  **Sample photo #1 COMPRESSED L85 (4.8MB)**
  ![compressed](/images/compressed_85.jpg)
  
  **Sample photo #1 COMPRESSED L50 (2.5MB)**
  ![compressed](/images/compressed_50.jpg)

 > [!NOTE]
 > "Compress photos" allows you to significantly reduce the size of photo files (2-5 times) with little loss of quality. The example above uses a compression value of 50 (range 1 to 99) and reduces the file size by a factor of 4.5 while keeping the resolution of the photo the same!

 ## Remarks
 - All file names in folders (subfolders) are obfuscated, but folder (subfolder) names are NOT obfuscated.
 - All file extensions are converted to lower case (force).
 - There is a special option to save filenames sorted by first letter.
 - Compression also removes all metadata from photos (e.g. device and location information).
 - The system also automatically analyses and identifies duplicate files (different names but same content) along the specified path before processing begins.