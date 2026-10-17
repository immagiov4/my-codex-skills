# Compose applications and dashboards

Connect each component to actual application data and states. Animation accompanies transitions between those states.

## Index

- [A01 · An assistant composer with actual request states](#a01)

- [A02 · An activity indicator tied to a real phase](#a02)

- [A03 · A live chart with defined data and units](#a03)

- [A04 · A chart chosen for a specific question](#a04)

- [A05 · A dashboard assembled from free blocks](#a05)

- [A06 · Application controls using the existing component system](#a06)

- [A07 · An empty state with a useful next action](#a07)

- [A08 · An error state that supports recovery](#a08)

- [A09 · Progress based on completed steps](#a09)

- [A10 · A useful completion state](#a10)

- [A11 · A primary action with a clear visual hierarchy](#a11)

- [A12 · A searchable catalog organized by task](#a12)

## A01

### An assistant composer with actual request states

The input and response follow the service's real operation.

Procedure:

1. Choose free Beautiful UI/AICSS components or the project's existing composer.

2. Connect draft, sending, processing, reply, and error to actual states; preserve text and attachment or cancellation behavior supported by the service.

3. Adapt to the existing state management and test successful, slow, and failed requests with the same controls.

Source steps: [8GfWKFyAaW4 · 1:29](https://www.youtube.com/watch?v=8GfWKFyAaW4&t=89s), [8GfWKFyAaW4 · 8:20](https://www.youtube.com/watch?v=8GfWKFyAaW4&t=500s).

Result check: The interface reflects the real request and users retain the actions and input needed to recover.

## A02

### An activity indicator tied to a real phase

Listening, searching, or working is visible while the corresponding operation runs.

Procedure:

1. Use Thinking Orbs or Beautiful UI for the required operation state.

2. When duration is unknown, describe actual activity; show numeric progress only when the service supplies it.

3. Provide a text state for reduced motion and the cancellation or retry actions supported by the application.

Source steps: [Jhx7n9uAKHg · 1:56](https://www.youtube.com/watch?v=Jhx7n9uAKHg&t=116s), [SAxKK5fbjbc · 1:15](https://www.youtube.com/watch?v=SAxKK5fbjbc&t=75s).

Result check: The displayed phase follows the service and ends when the operation completes.

## A03

### A live chart with defined data and units

Liveline displays actual series with meaningful scale and update behavior.

Procedure:

1. Define the series source, scale, time interval, and units.

2. Integrate Liveline with real updates and explicit empty, stopped, and error states.

3. Provide an accessible summary or table and check the chart against its underlying values.

Source steps: [Jhx7n9uAKHg · 3:54](https://www.youtube.com/watch?v=Jhx7n9uAKHg&t=234s).

Result check: The plot matches the data, units are readable, and update or failure states remain understandable.

## A04

### A chart chosen for a specific question

A funnel, heatmap, or line chart answers an identified data question.

Procedure:

1. State the question and choose the appropriate Bklit UI chart.

2. Use actual data and the project's colors, labels, and layout.

3. Integrate the free chart code and verify values and states; treat Studio or video-export features as separate products.

Source steps: [9NubqbSNbjg · 3:08](https://www.youtube.com/watch?v=9NubqbSNbjg&t=188s).

Result check: Each chart answers a clear question, values agree with the data, and empty states remain meaningful.

## A05

### A dashboard assembled from free blocks

Navigation, summaries, and operational content share a coherent dashboard layout.

Procedure:

1. Choose available Efferd blocks; dashboards 1–5 were free at the 29 September 2026 verification.

2. Replace sample data and use native Codex images when available to match the palette.

3. Connect actual actions and test relevant loading, empty, and error states.

Source steps: [a_mZ4Kp3lTM · 0:00](https://www.youtube.com/watch?v=a_mZ4Kp3lTM&t=0s).

Result check: The dashboard uses real data and its controls work across the required states.

## A06

### Application controls using the existing component system

Forms and navigation use consistent controls and states.

Procedure:

1. Choose the needed coss ui or shadcn/ui controls, respecting existing dependencies.

2. Apply the anchor page's values to active, disabled, error, and focus states.

3. Test keyboard navigation and the actual application actions.

Source steps: [8GfWKFyAaW4 · 6:40](https://www.youtube.com/watch?v=8GfWKFyAaW4&t=400s).

Result check: Controls share a visual system and work with keyboard input and real states.

## A07

### An empty state with a useful next action

The empty view explains its cause and helps the user continue.

Procedure:

1. Identify the cause: first use, no matching results, or a completed task.

2. Provide the corresponding action: create content, change filters, or continue.

3. Add an original illustration only when it clarifies the state; test the proposed action.

Source steps: [SAxKK5fbjbc · 4:26](https://www.youtube.com/watch?v=SAxKK5fbjbc&t=266s).

Result check: The cause is understandable and the action resolves it or advances the task.

## A08

### An error state that supports recovery

A relevant message and action help recover without losing valid input.

Procedure:

1. Identify the failed field or operation and use the application's stable error message.

2. Offer the relevant correction, retry, or authentication recovery action while retaining valid data.

3. Trigger the actual error and verify the complete recovery path.

Source steps: [SAxKK5fbjbc · 6:03](https://www.youtube.com/watch?v=SAxKK5fbjbc&t=363s).

Result check: The user can understand the failure, preserve valid input, and complete the recovery.

## A09

### Progress based on completed steps

A multi-step task shows actual completion and the next action.

Procedure:

1. Define the real steps and calculate completed steps against the total.

2. Show the current position and next action while retaining supported editing and back navigation.

3. Test resuming from saved state and confirm that the indicator reflects it.

Source steps: [MVOpq3WRnbo · 0:34](https://www.youtube.com/watch?v=MVOpq3WRnbo&t=34s).

Result check: Progress corresponds to completed work and the task can resume from its actual saved state.

## A10

### A useful completion state

The final view identifies the completed result and what can happen next.

Procedure:

1. Connect success to the actual completion of the operation.

2. Present the resulting booking, file, or other outcome and its useful next action.

3. Optionally add a brief original animation while retaining available controls and a readable reduced-motion state.

Source steps: [MVOpq3WRnbo · 1:30](https://www.youtube.com/watch?v=MVOpq3WRnbo&t=90s).

Result check: The final result is identifiable and its next action works immediately.

## A11

### A primary action with a clear visual hierarchy

The task's main action is easy to find among available choices.

Procedure:

1. Identify the primary task action and retain access to the other options.

2. Use hierarchy, shape, color, and an appropriate icon to make that action recognizable.

3. Test actual labels, keyboard focus, and reduced contrast; the distinction should remain understandable beyond color.

Source steps: [MVOpq3WRnbo · 3:58](https://www.youtube.com/watch?v=MVOpq3WRnbo&t=238s).

Result check: The intended action is recognizable and all required options remain reachable.

## A12

### A searchable catalog organized by task

Groups, names, search, and filters help users find the requested option.

Procedure:

1. Group and name items according to the user's actual task.

2. Add search or filters appropriate to the catalog and retain access to the complete list.

3. Test matching results, an empty result, and resetting the search or filters.

Source steps: [MVOpq3WRnbo · 5:03](https://www.youtube.com/watch?v=MVOpq3WRnbo&t=303s).

Result check: The requested item can be found and the full catalog can be restored.
