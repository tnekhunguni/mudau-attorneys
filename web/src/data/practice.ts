// Practice area content. Each entry becomes /practice-areas/<slug>/.
// Keep claims factual: no "expert", "specialist" or outcome promises (LPC Code of Conduct).

export type Practice = {
  slug: string;
  group: 'people' | 'organisations';
  name: string;
  summary: string;      // one line, used in lists
  intro: string;        // opening paragraph on the page
  services: string[];   // what we do
  timeLimits?: { title: string; detail: string }[];
  bring?: string[];     // what to bring to the first consultation
  faqs?: { q: string; a: string }[]; // shown on the page and as FAQ structured data
  description: string;  // meta description
};

export const practices: Practice[] = [
  {
    slug: 'criminal-litigation',
    group: 'people',
    name: 'Criminal litigation',
    summary: 'Bail applications, trials, representations to the NPA and appeals.',
    intro:
      'If you or a family member has been arrested or charged, the first days matter most. We advise on your rights, apply for bail and represent you through to trial, sentence and appeal.',
    services: [
      'Advice after arrest and at the police station',
      'Bail applications and bail appeals',
      'Representations to the National Prosecuting Authority to withdraw or reduce charges',
      "Trials in the District, Regional and High Courts",
      'Plea and sentence proceedings',
      'Appeals and reviews',
      'Fraud and commercial crime, including forensic investigation of the facts',
    ],
    bring: [
      'The charge sheet, J88 or any documents the police gave you',
      'The case number and the police station handling it',
      'Names and numbers of any witnesses',
      'Your next court date, if one has been set',
    ],
    faqs: [
      { q: "Can I get bail?", a: "Most people charged with an offence can apply for bail. The court considers things like the seriousness of the charge, whether you are likely to stand trial and whether you might interfere with witnesses. For some serious offences you have to show exceptional circumstances or that your release is in the interests of justice, so preparation matters." },
      { q: "Should I give the police a statement?", a: "You have the right to remain silent and the right to a legal representative. Speak to an attorney before making any statement or signing anything." },
    ],
    description: 'Criminal litigation attorneys in Thohoyandou, Limpopo: bail applications, trials, representations to the NPA and appeals.',
  },
  {
    slug: 'labour-disputes',
    group: 'people',
    name: 'Dismissals and workplace disputes',
    summary: 'Unfair dismissal and labour matters at the CCMA, bargaining councils and the Labour Court.',
    intro:
      'If you have been dismissed, suspended or treated unfairly at work, we explain where you stand and represent you at the CCMA, the relevant bargaining council or the Labour Court.',
    services: [
      'Unfair dismissal and unfair labour practice disputes',
      'Representation at conciliation and arbitration',
      'Disputes before bargaining councils',
      'Labour Court referrals, reviews and applications',
      'Advice on retirement fund, pension and medical aid rights',
      'Reviewing settlement and separation agreements before you sign',
    ],
    timeLimits: [
      { title: 'Unfair dismissal', detail: 'Refer the dispute to the CCMA or bargaining council within 30 days of the dismissal.' },
      { title: 'Unfair labour practice', detail: 'Refer within 90 days of the act or omission, or of when you became aware of it.' },
      { title: 'Unfair discrimination', detail: 'Refer within 6 months of the act or omission.' },
    ],
    bring: [
      'Your employment contract and recent payslips',
      'The dismissal letter, notice of hearing or any written warnings',
      'Minutes or notes from any disciplinary hearing',
      'Any messages or emails relevant to the dispute',
    ],
    faqs: [
      { q: "How long do I have to challenge my dismissal?", a: "Refer the dispute to the CCMA or your bargaining council within 30 days of the dismissal. If you are late you must apply for condonation, which is not guaranteed." },
      { q: "Can an attorney represent me at the CCMA?", a: "Legal representation is generally not allowed at conciliation. At arbitration it depends on the type of dispute and may need the commissioner's agreement. We prepare your case in every forum and represent you wherever the rules allow, including at bargaining councils and the Labour Court." },
    ],
    description: 'Unfair dismissal and labour dispute attorneys in Thohoyandou, Limpopo: CCMA, bargaining council and Labour Court representation.',
  },
  {
    slug: 'civil-litigation',
    group: 'people',
    name: 'Civil litigation',
    summary: 'Disputes over money, contracts and property, and defending a summons against you.',
    intro:
      'If someone owes you money, has broken an agreement with you, or has issued a summons against you, we explain your options and represent you in the Magistrate\'s Courts and the High Court.',
    services: [
      'Claims for money owed and breach of contract',
      'Defending a summons or a claim against you',
      'Setting aside (rescinding) judgments granted against you',
      'Property, building and neighbour disputes',
      'Claims for damages',
      'Settlement negotiations and mediation',
    ],
    timeLimits: [
      { title: 'If you received a summons', detail: 'You generally have 10 court days to give notice that you intend to defend it, or judgment can be granted against you.' },
      { title: 'Claiming money owed', detail: 'Most ordinary debts prescribe 3 years after they became due.' },
    ],
    bring: [
      'The summons, letter of demand or court papers you received',
      'Any written agreement, quote or invoice',
      'Proof of payments and relevant messages or emails',
      'Your ID',
    ],
    faqs: [
      { q: "What should I do if I receive a summons?", a: "Don't ignore it. You generally have 10 court days to give notice that you intend to defend, otherwise the other side can ask for judgment against you. Bring the summons to us as soon as you receive it." },
      { q: "Can a judgment against me be set aside?", a: "Often, yes. If judgment was granted without you defending, you can apply to rescind it, generally within 20 court days of finding out about it. You must explain why you didn't defend and show you have a defence." },
    ],
    description: 'Civil litigation attorneys in Thohoyandou, Limpopo: money claims, contract and property disputes, and defending a summons.',
  },
  {
    slug: 'medical-negligence',
    group: 'people',
    name: 'Medical negligence',
    summary: 'Claims for harm caused by negligent treatment at public or private health facilities.',
    intro:
      'When treatment at a clinic or hospital causes avoidable harm, you may have a claim for damages. We investigate what happened, obtain the records and expert opinions, and litigate the claim.',
    services: [
      'Assessing whether the treatment fell below the expected standard',
      'Obtaining hospital and clinic records',
      'Briefing independent medical experts, with your written permission first',
      'Claims against provincial health departments and private facilities',
      'Birth injury and maternity claims',
      'Settlement negotiations and High Court litigation',
    ],
    timeLimits: [
      { title: 'Claims against the state', detail: 'Written notice must reach the relevant department within 6 months of the date the debt became due.' },
      { title: 'All claims', detail: 'A claim generally prescribes 3 years after you knew, or should have known, the facts it is based on.' },
    ],
    bring: [
      'Your hospital file number, clinic card or road-to-health booklet',
      'Dates of admission, treatment and discharge',
      'Names of the facility and, if known, the doctors or nurses involved',
      'Any medical reports or death certificate',
    ],
    faqs: [
      { q: "How long do I have to claim?", a: "For claims against a provincial health department, written notice must be given within 6 months. Most claims prescribe 3 years after you knew, or should have known, the facts. Contact us early because records and expert reports take time." },
      { q: "Do I need to get my medical records myself?", a: "No. We request the records from the hospital or clinic on your behalf, using the Promotion of Access to Information Act where necessary." },
    ],
    description: 'Medical negligence attorneys in Thohoyandou, Limpopo: claims against public and private hospitals and clinics.',
  },
  {
    slug: 'personal-injury',
    group: 'people',
    name: 'Personal injury and unlawful arrest',
    summary: 'Road Accident Fund claims, unlawful arrest and detention, and other damages claims.',
    intro:
      'If you were injured in a road accident, or arrested and detained without lawful grounds, you may be entitled to compensation. We lodge and run the claim for you.',
    services: [
      'Road Accident Fund claims for injury and loss of support',
      'Unlawful arrest and detention claims against the Minister of Police',
      'Malicious prosecution claims',
      'Defamation claims',
      'Other claims for injury to person or property',
    ],
    timeLimits: [
      { title: 'Road Accident Fund', detail: 'Lodge the claim within 3 years of the accident, or within 2 years if the driver was never identified (hit-and-run).' },
      { title: 'Claims against the police', detail: 'Written notice must reach the Minister of Police within 6 months of the arrest or release.' },
    ],
    bring: [
      'The accident report and police case number',
      'Hospital records and any medical reports',
      'Your ID and proof of income before the accident',
      'For unlawful arrest: release documents, charge sheet or court record',
    ],
    faqs: [
      { q: "How long do I have to claim from the Road Accident Fund?", a: "Three years from the accident if the driver is known, or two years for a hit-and-run. If the claim is not settled, a summons must generally be issued within five years of the accident." },
      { q: "Can I claim if I was a passenger or pedestrian?", a: "Yes. Passengers, pedestrians and drivers who were not at fault can claim, as can dependants of a person killed in an accident." },
    ],
    description: 'Road Accident Fund, unlawful arrest and personal injury attorneys in Thohoyandou, Limpopo.',
  },
  {
    slug: 'family-and-estates',
    group: 'people',
    name: 'Family law, wills and estates',
    summary: 'Divorce, maintenance and care of children, drafting wills and winding up estates.',
    intro:
      'Family matters are personal and often urgent. We handle them with discretion, and look for agreed solutions before going to court where that serves you and your children.',
    services: [
      'Divorce, including civil and customary marriages',
      'Maintenance claims and enforcement',
      'Parenting plans, care and contact arrangements for children',
      'Domestic violence protection orders',
      'Drafting wills',
      'Reporting and winding up deceased estates with the Master of the High Court',
    ],
    bring: [
      'Your ID and marriage certificate or proof of customary marriage',
      "Children's birth certificates",
      'Any existing court orders or maintenance orders',
      'For estates: the death certificate and any will',
    ],
    faqs: [
      { q: "What happens if someone dies without a will?", a: "Their estate is divided according to the Intestate Succession Act, which may not match what they would have wanted. A valid will lets you decide who inherits and who administers your estate." },
      { q: "How is child maintenance decided?", a: "Both parents have a duty to support their children. The Maintenance Court looks at what the child reasonably needs and what each parent can afford." },
    ],
    description: 'Family law, divorce, maintenance, wills and deceased estates attorneys in Thohoyandou, Limpopo.',
  },
  {
    slug: 'employment-law',
    group: 'organisations',
    name: 'Employment law for employers',
    summary: 'Chairing disciplinary hearings, CCMA representation, workplace investigations and policies.',
    intro:
      'We help employers in the public and private sectors run fair procedures, resolve disputes and stay compliant with labour legislation.',
    services: [
      'Chairing and initiating disciplinary hearings',
      'Representing employers at the CCMA, bargaining councils and the Labour Court',
      'Workplace and forensic investigations',
      'Employment contracts, policies and procedures',
      'Collective bargaining, strikes and restructuring',
      'Employment equity and basic conditions of employment advice',
      'Labour law training for managers and staff',
    ],
    faqs: [
      { q: "Can we dismiss an employee without a hearing?", a: "A dismissal must be for a fair reason and follow a fair procedure. That normally means telling the employee what the allegations are and giving them a proper chance to respond. We can chair or initiate the hearing so the process stands up later." },
      { q: "Is a CCMA arbitration award final?", a: "Yes, it is binding. It can only be taken on review to the Labour Court on limited grounds, generally within six weeks of the award." },
    ],
    description: 'Employment law for employers in Limpopo: disciplinary hearings, CCMA representation, investigations and policies.',
  },
  {
    slug: 'litigation',
    group: 'organisations',
    name: 'Civil and High Court litigation',
    summary: "Opinions, pleadings and appearances in the Magistrate's Courts and the High Court.",
    intro:
      "We litigate for and against individuals, companies and public institutions in the Magistrate's Courts and the High Court, and brief counsel where a matter needs it.",
    services: [
      'Legal opinions and memoranda on litigation prospects',
      'Drafting pleadings, notices and applications',
      "Appearances in the Magistrate's Courts and the High Court",
      'Urgent applications and interdicts',
      'Contract and property disputes',
      'Mediation and arbitration',
    ],
    faqs: [
      { q: "Which court will our matter go to?", a: "It depends on the amount claimed and the nature of the dispute. Smaller claims are heard in the Magistrates' Courts and larger or more complex matters in the High Court. We advise on the court that is appropriate and most cost-effective." },
      { q: "Will you brief an advocate?", a: "Where a matter needs counsel, we brief an advocate only after you have approved it in writing." },
    ],
    description: "Civil litigation attorneys in Thohoyandou, Limpopo, acting in the Magistrate's Courts and High Court across South Africa.",
  },
  {
    slug: 'commercial-law',
    group: 'organisations',
    name: 'Commercial, contracts and corporate',
    summary: 'Drafting and reviewing agreements, governance, board charters and trade marks.',
    intro:
      'We draft, review and negotiate the agreements a business runs on, and advise boards and management on governance and compliance.',
    services: [
      'Drafting, reviewing and interpreting commercial agreements',
      'Policies and board charters',
      'Governance reviews and regulatory compliance advice',
      'Intellectual property: trade marks, copyright and transfer of ownership',
      'Construction and building agreements',
      'Commercial and corporate litigation',
    ],
    faqs: [
      { q: "Does an agreement have to be in writing?", a: "Most agreements are valid even if verbal, but some must be in writing to be enforceable, such as the sale of land. A clear written contract prevents disputes about what was agreed." },
      { q: "Can you help us register a trade mark?", a: "Yes. We advise on trade mark protection and prepare applications to the Companies and Intellectual Property Commission (CIPC)." },
    ],
    description: 'Commercial and contract attorneys in Limpopo: agreements, governance, board charters and intellectual property.',
  },
  {
    slug: 'debt-recovery',
    group: 'organisations',
    name: 'Debt recovery',
    summary: 'Letters of demand, acknowledgements of debt, default judgments, execution and section 65 enquiries.',
    intro:
      'We recover money owed to businesses, institutions and individuals, from the first letter of demand to execution against the debtor. The firm is registered with the Council for Debt Collectors.',
    services: [
      'Letters of demand and notices under the National Credit Act',
      'Acknowledgements of debt and payment arrangements',
      'Summons and default judgments',
      'Warrants of execution and attachments',
      'Section 65 financial enquiries',
      'Listing defaulters with credit bureaus',
    ],
    faqs: [
      { q: "When does a debt prescribe?", a: "Most ordinary debts prescribe 3 years after they became due, so act before then. A judgment debt lasts much longer, which is why getting judgment matters." },
      { q: "What is a section 65 enquiry?", a: "A court process in which a debtor with a judgment against them must disclose their income and expenses. The court can then order them to pay in instalments." },
    ],
    description: 'Debt collection and recovery attorneys in Thohoyandou, Limpopo: demands, default judgments, execution and section 65 enquiries.',
  },
  {
    slug: 'public-sector',
    group: 'organisations',
    name: 'Public sector, procurement and administrative law',
    summary: 'Advice on the PFMA and public procurement, agreements between organs of state and policy review.',
    intro:
      'We advise and act for organs of state, municipalities and institutions, and for businesses dealing with them.',
    services: [
      'Advice on the Public Finance Management Act',
      'Public procurement advice and procurement policies',
      'Drafting and negotiating agreements between organs of state',
      'Public-private partnerships',
      'Reviews of administrative decisions',
      'Constitutionality of legislation and policies',
      'Commentary on national and provincial bills',
    ],
    faqs: [
      { q: "Do you act for municipalities?", a: "Yes. Mr Mudau has acted for municipalities including Thulamela Municipality and the City of Ekurhuleni, and for public institutions such as the University of Venda." },
      { q: "Can a procurement decision be challenged?", a: "Yes. Bidders can use internal objection processes and, where necessary, apply to the High Court to review the decision. We act for bidders and for organs of state defending their decisions." },
    ],
    description: 'Public sector, procurement, PFMA and administrative law attorneys for municipalities and institutions in Limpopo.',
  },
];

export const practicesFor = (group: Practice['group']) => practices.filter((p) => p.group === group);
