This repository contains sample plugins for [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme). 

To run and debug:
1. Set your IDE's run configuration to run the `yt_dlp` Python module.
2. Add your project's root directory containing `ytdlp_plugins` to `PYTHONPATH` environment variable (this may not be necessary with some IDE run configurations)
3. The `ytdlp_plugins` folder should be automatically picked up by yt-dlp (run with `-v` to check)

You can install them using pip with:
```
python3 -m pip install -U https://github.com/yt-dlp/ytdlp-sample-plugins/archive/master.zip
```

See [yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#plugins) for more details
