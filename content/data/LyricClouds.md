Title: Lyric clouds, genre maps and distinctive words
Date: 2014-06-04
Tags: music, lyrics, lastfm, IR, visualization
Summary: Repost of an article I wrote for the Last.fm blog in 2011. What do different genres of music look like if you visualize the words used in their lyrics? The results are... Eye-opening.

*This is a repost of an [article](http://blog.last.fm/2011/06/22/lyric-clouds-genre-maps-and-distinctive-words) I wrote for the Last.fm blog while working there in 2011. The images disappeared from Last.fm so I'm serving them out of the wonderful [Internet Archive](http://web.archive.org).*

One of the interesting things that sets even superficially similiar genres of music apart is their lyrical content. Last.fm tags can overlap to a great degree, but we were interested to see what the words can tell you about the subtler shades of meaning that go along with those tags. As usual around here, the best way to answer questions like these is by asking the data.

So I downloaded the [musiXmatch dataset][1], a collection of lyric tables for nearly 240,000 songs from all around the world (and the musical universe). They are tables in the sense that they don't contain the intact lyrics of each song, but rather a list of words present in each song, along with the number of times that word occurs. No use for karaoke, but perfect for investigating the overall properties of a genre. I then matched up the songs in the dataset with tracks in our own catalogue, and correlated this with Last.fm tag data, in order to count the number of times a given word appeared in each of several prominent genres.

#### Lyric clouds

Of course, lists of words and frequencies are a little dry, but thankfully IBM have released a [Word-Cloud Generator][2] which can take a weighted list of words and display it graphically, as seen on the [Wordle][3] website. The more often a word appears, the bigger it will be rendered. Here's what it came up with for the genres I tried — the software did the layout, but you can blame me for the font selection.

<br/>
<table>
    <tbody><tr>
        <td align="center" valign="middle" width="200">
            <i>Click to open full images in a new window.<br><br>
                <b>Warning: they contain lyrics you may find offensive. Not safe for work.</b></i>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/blues.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/blues_thumb.png"><br>
Blues
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/country.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/country_thumb.png"><br>
Country
            </a>
        </td>
    </tr>
    <tr><td colspan="3">&nbsp;</td></tr>
    <tr>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/electronic.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/electronic_thumb.png"><br>
Electronic
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/folk.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/folk_thumb.png"><br>
Folk
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/goth.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/goth_thumb.png"><br>
Goth
            </a>
        </td>
    </tr>
    <tr><td colspan="3">&nbsp;</td></tr>
    <tr>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/hip-hop.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/hip-hop_thumb.png"><br>
Hip-hop
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/indie.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/indie_thumb.png"><br>
Indie
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/metal.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/metal_thumb.png"><br>
Metal
            </a>
        </td>
    </tr>
    <tr><td colspan="3">&nbsp;</td></tr>
    <tr>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/rap.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/rap_thumb.png"><br>
Rap
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/rock.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/rock_thumb.png"><br>
Rock
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/1/soul.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/1/soul_thumb.png"><br>
Soul
            </a>
        </td>
    </tr>
</tbody></table>
<br/>


I did a bit of pre-processing to remove common 'stopwords' that don't really hold any information about the topics of the lyrics (and, for, I, you, the, plus many more), but this only took into account English words — and if you look closely, you'll see a few common words from German, French and Spanish (and probably others) that are from foreign-language songs in the dataset. But what's most striking for me about these is not how much they differ, but in fact how often some of the words appear prominently across genres. Almost everyone sings about love, for example, with the exception of Rap and Hip-Hop, and time comes up… time and time again.

#### Genre maps

A limitation of word clouds is that while they're great for showing the comparative popularity of words within a genre, they're not so good for looking at the overall similarities or differences of several genres at once. To do that, you need some measure of similarity which can be rendered graphically as a kind of 'genre neighbourhood map'. So I measured the similarities between the word lists for each genre, ranked by popularity, using [a method][4] which was developed to compare the result rankings from different search engines. This gives a single value for how similar the lyric choices are between each pair of genres, where differences towards the top of the lists (the most popular words) are considered more important than differences further down. A bit of [extra number crunching][5] in [R][6] can convert these similarity scores into a 2D map, which I imported into [OpenOffice][7] to render:

<a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/lyric_map.png" target="wordle"><br>
<img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/lyric_map_small.png"><br>
</a>

*Click image to open larger version in a new window.*

This map is really interesting for its combination of expected and unexpected neighbours, and also for the way it clearly shows Rap and Hip-Hop as outliers from the main axis on the left. Goth and Metal, which may appear similar to the un-trained ear (and eye!), are considerably separated, while Metal and Folk are — surprisingly — much closer. Electronic (a very broad tag) is clustered together with Soul and Blues, presumably because of the soulful origins of house music, which is one of the more lyrical electronic sub-genres. And Rap and Hip-Hop, which might be considered synonymous by the layman, are about as different as Indie and Country in terms of lyric ranking.

#### Distinctive words

The word clouds as shown draw the viewer's attention to the very frequent words, but these also tend to be the ones like love and time which are popular across genres. This is a problem if you want to find out which words are most distinctive or characteristic of a given genre — the words which, if used as search terms for example, would be best at selecting songs from that genre correctly (true positives), while minimizing the number of songs retrieved from other genres (false positives). Once again, information retrieval (the science behind search engines) can help us — the F measure or [F score][9] is specifically designed for measuring the tradeoff between true positives and false positives in a set of results. It's a score between 0 and 1, where 0 means "no relevant documents retrieved", but 1 means "all relevant documents retrieved" and "no additional spurious documents retrieved".

So I calculated the F score that each word would have as a search term for each genre in some notional lyric-based search engine: "how relevant would the results be if I searched for Indie tracks with the search term friend" for example. This doesn't take into account the number of times each word occurs within a song, just the fact that it occurs at all, but it does let us redraw the lyric clouds with each word's size determined by its F score for that genre. As you can see, this brings out the words that are characteristic of each genre, rather than emphasizing those that are globally popular:

<br/>
<table>
    <tbody><tr>
        <td align="center" valign="middle" width="200">
            <i>Click to open full images in a new window.<br><br>
                <b>Warning: they contain lyrics you may find offensive. Not safe for work.</b></i>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/blues.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/blues_thumb.png"><br>
Blues
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/country.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/country_thumb.png"><br>
Country
            </a>
        </td>
    </tr>
    <tr><td colspan="3">&nbsp;</td></tr>
    <tr>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/electronic.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/electronic_thumb.png"><br>
Electronic
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/folk.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/folk_thumb.png"><br>
Folk
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/goth.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/goth_thumb.png"><br>
Goth
            </a>
        </td>
    </tr>
    <tr><td colspan="3">&nbsp;</td></tr>
    <tr>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/hip-hop.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/hip-hop_thumb.png"><br>
Hip-hop
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/indie.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/indie_thumb.png"><br>
Indie
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/metal.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/metal_thumb.png"><br>
Metal
            </a>
        </td>
    </tr>
    <tr><td colspan="3">&nbsp;</td></tr>
    <tr>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/rap.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/rap_thumb.png"><br>
Rap
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/rock.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/rock_thumb.png"><br>
Rock
            </a>
        </td>
        <td align="center" valign="middle" width="200">
            <a href="http://web.archive.org/web/20120107121411/http://users.last.fm/~andy/lyric_clouds/2/soul.png" target="wordle">
                <img src="http://web.archive.org/web/20120107121411im_/http://users.last.fm/~andy/lyric_clouds/2/soul_thumb.png"><br>
Soul
            </a>
        </td>
    </tr>
</tbody></table>
<br/>

I think they bring out the unique character of each genre much more effectively, and the variation in size between the words is much less, so the less prominent words are easier to see. There are some interesting quirks visible too. For example, many German words are much more clearly visible in the Goth cloud than they were before, reflecting both the comparatively large number of songs in German in that genre, and the lack of German lyrics in most other genres. Country for example is entirely English.

Finally, a little extra present from the data. The word with the highest F score in the whole dataset is Christmas, with an F score of 0.3892 for the tag… Christmas. So, unseasonal greetings from the data crunchers here at Last.HQ!

*Thanks to [musiXmatch][10] for making the lyric database available, and [Thierry Bertin-Mahieux][11] for helping me to reconstruct the full words from the stems in the database.*

[1]: http://labrosa.ee.columbia.edu/millionsong/musixmatch
[2]: http://www.alphaworks.ibm.com/tech/wordcloud
[3]: http://www.wordle.net/
[4]: http://blog.codalism.com/?p=1317
[5]: http://www.statmethods.net/advstats/mds.html
[6]: http://www.r-project.org/
[7]: http://www.openoffice.org/
[9]: http://en.wikipedia.org/wiki/F-score
[10]: http://musixmatch.com/
[11]: http://www.columbia.edu/~tb2332/
  

