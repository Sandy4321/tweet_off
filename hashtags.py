employers = {
    'hr',
    'humanresources',
    'recruiting',
    'hiring',
    'talentacquisition',
    'leadership',
    'hrtech',
    'hru',
    'socialrecruiting',
    'sourcing',
    'recruitingtrends',
    'recruitingprocess'
}
job_seekers = {
    'careers',
    'employment',
    'gethired',
    'hiring',
    'hiringcontractors',
    'nowhiring',
    'jobfairy',
    'joblisting',
    'jobopening',
    'jobposting',
    'jobs',
    'tweetmyjobs',
    'job',
    'unemployed',
    'needajob',
    'rtjobs',
    'jobsearch',
    'hireme'
}
job_tips = {
    'interviewtips',
    'jobadvice',
    'jobsearchtips',
    'jobtips',
    'jobhunt',
    'jobseekers',
}
career_tips = {
    'careeradvice',
    'careerchange',
    'cv',
    'resume',
    'resumes',
    'resumeadvice',
    'resumetips',
    'resumewriting'
}
extras = {
    'manage',
    'hirefaster',
    'candidates',
    'talent',
    'talentsneeded',
    'techtalents',
    'datascience',
    'datadatadata',
    'machinelearning',
    'recruitingsoftware',
    'recruitingtech',
    'hiringplatform',
    'recruitingplatform',
    'oldATS',
    'ATS',
    'hirehirehire',
    'coffee',
    'lookingforwardtotheweekend',
    'wantmoreengineers',
    'wheretofinddevelopers',
    'poorrecruiters',
    'cantcatchabreak',
}

all_hashtags = employers | job_seekers | job_tips | career_tips | extras
text_capture_hashtags = employers | job_tips | career_tips

max_hashtag_length = len(max(all_hashtags, key=len)) + 1  # plus 1 for the hashtag-mark
