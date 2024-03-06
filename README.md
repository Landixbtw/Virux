# Virux_eSports

Commissioned bot by Virux_eSports, with following features requested. <br>

## Using the Bot - Join to create

[Join to create voice Channel]. Dafür muss ein Voice Channel vorhanden sein der, <code>join_for_voice</code> heißt. <br>
Sobald jemand in den Voice Channel joint, wird in der Selben Kategorie, ein Channel mit dem Tag der Person erstellt. <br>
![example for created channel](./pictures/channel_example.png)
<br>
Sobald der ersteller der Channels diesen verlässt, wird der Channel gelöscht. <br>
In den Audit-Logs ist das dann so zu sehen. <br>
![example in audit_logs one](./pictures/audit_log_example_1.png)
![example in audit_logs two](./pictures/audit_log_example_2.png)

## Using the Bot - Apply

[Bewerbungssystem]. Für das Bewerbungssystem muss ein Text Channel <code>bewerbungen</code> vorhanden sein. <br>
In den <code>bewerbungen</code> schickt der Bot die Bewerbungen rein. Mit <code>!button</code> kann man einen "apply"-button in den Channel schicken lassen in welchem man diesen ausführt. <br>
Sobal jemand das auf den Button Klick popt dieses Menü auf. <br>
![Example on how the Apply Modal looks](./pictures/modal_example.png)

Nachdem die Bewerbung erfolgreich abgeschickt wurde, bekommt der Bewerber eine Bestätigung und die bewerbung wird in den channel <code>bewerbungen</code>, geschickt. <br>

![Example on how it looks after a successfull application](./pictures/successfull_application.png)

Bewerbung für das Team im Bewerbungschannel<br>

![Application for the server team in the application channel](./pictures/application_for_team.png)

## How to use [Discohook](https://discohook.org)

Wie man eine Webhook von Discord bekommt. In den Server Einstellungen folgendes wählen. <br>
![getting a Webhook from Discord](./pictures/using_discohook_discord.png)

Bevor man die die Webhook abschickt oder den Link in Discohook eingibt muss man, den Namen, das Bild und den Channel festlegen. <br>
![setting up the Webhook](./pictures/setting_up_the_webhook.png)

Kopiere die Webhook url. <br>
![copying the webhook url](./pictures/copy_webhook_url.png)

Um die Webhook zu nutzen muss man als erstes allen clearen. <br>
![clearing all](./pictures/clear_all.png)

Füge die Webhook, hier ein ↓. <br>
![pasting the webhook url](./pictures/paste_webhook_url.png)

Was hier als Author oder Title geschrieben ist, ist in dem Menü als solches zu finden. <br>
![helping with understanding the embed](./pictures/embed_example.png)
