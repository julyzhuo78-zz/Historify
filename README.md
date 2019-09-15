# Historify - Hack the North 2019 Finalist 
![alt text](https://raw.githubusercontent.com/julyzhuo78/Historify/july2/static/Logo.png)

## Inspiration
When people visit the doctors office today, they rarely have more than 10 minutes to explain their problems and potential concerns they may have. Even worse, studies show that the average time you have before a doctor will interrupt you is 11 seconds!!! How much can you possibly explain in 11 seconds? Maybe one symptom you're having, but good luck trying to fit in your concern that your close friend recently had similar symptoms that escalated and resulted in an amputated arm. Or that you lost your job last month, don't have valid health insurance and can't afford even the cheapest medications. Or that, despite the best treatment plan being a combination of medications and minor surgery, this is against your culture that prioritizes spiritual and natural therapies.

The fault doesn't lie within the doctor necessarily, systematic healthcare constraints prevent the doctor from spending an extended amount of time with each patient. As a result, patients lose trust in their relationship with their doctor, adhere less to their treatment plan, and the doctor may also suggest options that aren't the most appropriate because they don't have a complete overview of the patient's presenting situation. But it wasn't always this way - medical students during training will spend ~1 hour with patients digging in to understand as much as they possibly could and gain a holistic view of the patients current symptoms, emotions, family history, social history, and more.

Furthermore, problems such as non-adherence to treatment plans cost the healthcare system upwards of $300 billion.

The solution? Collecting the patient history prior to the visit rather than during the 11 seconds at the beginning. This needs to be done in a convenient and user friendly manner to maximize adoption by the general population while simultaneously generating an output that is short enough for the doctor to quickly glance over and hit the ground running at the beginning of each patient encounter. That's exactly where Historify comes in.

## What it does
Historify is a conversation voice-user interface (VUI), white-labelled to the doctor/clinic and deployed via a smart speaker. Prior to a scheduled appointment, Historify will prompt the patient to interact with an intelligent series of questioning which collects their detailed history - significantly more than what can be obtained in 11 seconds. This interaction is conversational in nature as this has been shown to maximize patient engagement and develop an increased feeling of trust/openness. In addition, the questioning is reactive to the patient's responses and is broken into 2 parts.

The first part is a generic set of questions that applies to most conditions and includes the patients social/family history. The second component contains questions specific ONLY to the patient's current complaint. This is done by tapping into a library of medical conditions (with their associated symptoms, diagnosis, tests, etc.) and a logical tree that tries to distinguish between various medical diagnoses. This is reactive to the answers that are presented. Historify then takes all of this information and auto-generates a very simple patient history report that is sent to the physician to review for the appointment.

Importantly, one of the major use cases for Historify is its ability to deploy in numerous languages. Language barriers are a huge barrier to quality healthcare, particularly in remote settings. By completing their history prior to a visit, even if the patient doesn't speak the doctors language well the report can be translated automatically or using a professional translator to ensure everyone receives the highest quality treatment plan.

## How we built it
Our team's focus was on building an MVP that could drive a conversation with a patient, collect their history, and then generate a report that could be viewed externally by a doctor. We constructed several medical templates of all the pertinent information that is desirable to obtain when gathering a patient history and researched different medical conditions that can be associated with chest pain as a starting test.

We then used Voiceflow's platform to construct the conversational interface that would interact with a patient remotely, gather the required information and store it on google cloud. We then also designed a website to imitate what the doctor's screen might look like and pulled the data into a report.

## Challenges we ran into
Initially we were focusing on using certain technology and trying to force it into a solution which led us nowhere. We adapted and focused on discovering a problem that we were passionate about solving, which led us to the concept of collecting patient history. Prior to this, none of us had any experience designing conversational voice interfaces or using Voiceflow, so this was a completely new area for us to learn from scratch.

## What's next for Historify
We feel that Historify has a ton of potential to streamline many of the problems that healthcare currently faces related to time constraints. Stemming from the history collection, we can integrate existing APIs related to medical diagnosis or develop this ourselves and determine a confidence % for a potential diagnosis. Using this, we can actually have suggested tests for likely diagnoses available on the doctor's screen and pre-populated with patient info to improve efficiency. Historify can also be deployed as a chatbot for patients who may have speech impediments or would prefer that over voice.

## Key Technology used
Flask, Voiceflow, Google Cloud

## How to run it
1. Open this [voiceflow link](https://creator.voiceflow.com/demo/19007027740719)
2. Conduct a full or partial conversation with our smart speaker simulator.
3. Open our [website](https://cool-app-12345.appspot.com).
4. You will see your information appearing there.

**All copyright reserved.**
