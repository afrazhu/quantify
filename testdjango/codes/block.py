import tushare as ts
valueIndustry = ts.get_industry_classified()
valueIndustry.to_json('/home/code/shares/block/industry.json',orient='records');
valueConcept = ts.get_concept_classified()
valueConcept.to_json('/home/code/shares/block/concept.json',orient='records');

