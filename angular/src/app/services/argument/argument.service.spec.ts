import { TestBed } from '@angular/core/testing';

import { ArgumentService } from './argument.service';

describe('ArgumentService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ArgumentService = TestBed.get(ArgumentService);
    expect(service).toBeTruthy();
  });
});
