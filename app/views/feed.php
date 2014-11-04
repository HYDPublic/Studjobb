<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title>Studjobb - De nyeste jobbene</title>
    <subtitle>Stillingsannonser for studenter</subtitle>
    <id>tag:studjobb.no,1993:/</id>

    <link rel="self" type="application/atom+xml" href="http://studjobb.no/rss"/>
    <link rel="alternate" type="text/html" href="http://studjobb.no/"/>

    <updated>2014-11-04T14:43:54-08:00</updated>

    <author>
        <name>Studjobb</name>
        <email>michael@studjobb.no</email>
        <uri>http://studjobb.no</uri>
    </author>

    <?php foreach ($jobs as $job): ?>
    <entry>
        <title><?php print $job->title; ?></title>
        <id>tag:studjobb.no,2012-05-25:1337969960</id>
        <link href="http://studjobb/stilling/<?php print $job->id; ?>"/>
        <updated>2012-05-25T18:19:20Z</updated>
        <published>2012-05-25T18:19:20Z</published>
        <content type="html"><![CDATA[

        ]]></content>
     </entry>
    <?php endforeach; ?>

</feed>
