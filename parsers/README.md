## goal
Parse pdfs into json files, each containing the text and metadata of **a single page** of the pdf file. 

## parsers
Each file in the parsers folder attempts to parse pdfs into json files. Having tried four different pdf parsers, here are some findings. 

### Papermage 
Papermage is a library developed specifically to parse scientific papers. It includes useful features such as classifying different parts of the paper into sections, header, footer, bibliography, sentences, tables etc... It can provide metadata quite accurately including titles, authors, and keywords. It takes about 20 hours to parse ~2400 pdfs totaling 3.86GB. A problem we encountered is that about a quarter of the papers were transcribed in CID or Character Identifier font. There is a significant loss of data for Korean pdfs. 

### Pypdf 
Pypdf is a PDF toolkit that retrieves text and manipulates pages of PDFs. I attempted to use Pypdf to remove table and figure data but did not succeed. 

### multilingual_pdf2text
Having encountered issues with Korean and CID while using papermage, I decided to give this library a go. I don't remember what the issue was but I ended up not using this library. 

### Tika
Tika is a content detection framework developed by Apache. It runs faster than Papermage (10 hours instead of 20). It does not have issues with Korean and CID. It is also capable of giving text by page. There were very few issues and not a lot of debugging/onboarding to do. Still has issues with tables data. 

## Conclusion
I used Apache Tika to retrieve text by page. I used Papermage to get metadata. After parsing, the JSON files' schema looks as such: 
```
{
    "pdf": string,
    "num_pages": number,
    "title": string,
    "author": string,
    "keyword": string,
    "url": string,
    "text": string,
    "pageNumber": number
}
```
See examples folder for a sample pdf file and its corresponding parsed jsons. 
