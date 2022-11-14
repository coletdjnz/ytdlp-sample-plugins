# coding: utf-8

# ⚠ Don't use relative imports
from yt_dlp.extractor.common import InfoExtractor


# ℹ️ Instructions on making extractors can be found at:
# 🔗 https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#adding-support-for-a-new-site

# ⚠ The class name must end in "IE"
class SampleExternalPluginGitHubIE(InfoExtractor):
    _WORKING = False
    IE_DESC = False
    _VALID_URL = r'^sampleplugingh:'

    def _real_extract(self, url):
        self.to_screen('URL "%s" sucessfully captured' % url)
