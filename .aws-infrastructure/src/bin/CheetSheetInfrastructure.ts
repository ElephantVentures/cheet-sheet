#!/usr/bin/env node
import 'source-map-support/register';
import cdk = require('@aws-cdk/core');
import { CheetSheetInfrastructureStack } from '../lib/CheetSheetInfrastructure-stack';

const app = new cdk.App();
new CheetSheetInfrastructureStack(app, 'CheetSheetInfrastructureStack');
