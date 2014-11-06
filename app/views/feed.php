<?php echo '<?xml version="1.0" encoding="utf-8"?>'; ?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title>Studjobb - De nyeste jobbene</title>
    <subtitle>Stillingsannonser for studenter</subtitle>
    <id>tag:studjobb.no,1993:/</id>

    <link rel="self" type="application/atom+xml" href="http://studjobb.no/rss"/>
    <link rel="alternate" type="text/html" href="http://studjobb.no/"/>

    <updated><?php echo (new DateTime($jobs[5]->created_at))->format('c'); ?></updated>

    <author>
        <name>Studjobb</name>
        <email>michael@studjobb.no</email>
        <uri>http://studjobb.no</uri>
    </author>

    <?php foreach ($jobs as $job): ?>
    <entry>
        <title><?php print trim($job->title); ?> - <?php print $job->company->name; ?></title>
        <id>http://studjobb.no/stilling/<?php print $job->id; ?></id>
        <link href="http://studjobb.no/stilling/<?php print $job->id; ?>"/>
        <published><?php echo (new DateTime($job->created_at))->format('c'); ?></published>
        <updated><?php echo (new DateTime($job->created_at))->format('c'); ?></updated>
        <content type="html"><![CDATA[
            <?php echo trim(str_replace('&nbsp;', ' ', strip_tags(implode(' ', array_slice(explode(' ', $job->content), 0, 75)), '<br>'))) . '...'; ?>
            <br><br>
            Frist: <?php echo $job->due(); ?>
            <br>
            <a href="http://studjobb.no/stilling/<?php print $job->id; ?>"><strong>Les mer</strong></a>
        ]]></content>
     </entry>
    <?php endforeach; ?>

</feed>
