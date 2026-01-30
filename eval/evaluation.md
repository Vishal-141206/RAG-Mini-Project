# Evaluation Results

The system was evaluated using a small set of representative questions designed
to test grounding, hallucination avoidance, and response clarity.

| Question | Expected Coverage | Result |
|--------|------------------|--------|
| What is the refund policy? | Fully answerable | ✅ |
| How long does refund processing take? | Fully answerable | ✅ |
| Can I cancel an order after it is shipped? | Fully answerable | ✅ |
| Are international returns supported? | Not covered | ❌ |
| Is there a cancellation fee for bulk orders? | Partially covered | ⚠️ |
| What payment methods are supported? | Not covered | ❌ |

**Scoring legend:**
- ✅ Correct and fully grounded answer 
- ⚠️ Partially supported by documents 
- ❌ Information not present (correct refusal)

The results show that the system consistently avoids hallucination and
prioritizes factual correctness over speculative responses.
